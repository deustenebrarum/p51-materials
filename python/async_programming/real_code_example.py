import asyncio

asyncio.create_task(_run_broadcast())
# 1.1
# 1.3
asyncio.create_task(_run_broadcast())
# 2.1
# 2.3
print(10)
# 10
# 2.4
# 2.5
# 2.6
# 2.7
# 1.4
# 1.5
# 2.8

self._lock = asyncio.Lock()

async def start_broadcast(self, broadcast_id: int, config: BroadcastConfig) -> None:
    if self._bot is None:
        logger.error("Невозможно запустить рассылку %s: бот не инициализирован", broadcast_id)
        await self._mark_failed(broadcast_id)
        return

    cancel_event = asyncio.Event()

    with await self._lock:
        if broadcast_id in self._tasks and not self._tasks[broadcast_id].task.done():
            logger.warning("Рассылка %s уже запущена", broadcast_id)
            return

        task = asyncio.create_task(
            self._run_broadcast(broadcast_id, config, cancel_event),
            name=f"broadcast-{broadcast_id}",
        )
        self._tasks[broadcast_id] = _BroadcastTask(task=task, cancel_event=cancel_event)
        task.add_done_callback(lambda _: self._tasks.pop(broadcast_id, None))


async def request_stop(self, broadcast_id: int) -> bool:
    async with self._lock:
        task_entry = self._tasks.get(broadcast_id)
        if not task_entry:
            return False

        task_entry.cancel_event.set()
        return True

async def _run_broadcast(
        self,
        broadcast_id: int,
        config: BroadcastConfig,
        cancel_event: asyncio.Event,
    ) -> None:
        sent_count = 0
        failed_count = 0

        try:
            if cancel_event.is_set():
                await self._mark_cancelled(broadcast_id, sent_count, failed_count)
                return

            async with AsyncSessionLocal() as session:
                broadcast = await session.get(BroadcastHistory, broadcast_id)
                if not broadcast:
                    logger.error("Запись рассылки %s не найдена в БД", broadcast_id)
                    return

                broadcast.status = "in_progress"
                broadcast.sent_count = 0
                broadcast.failed_count = 0
                await session.commit()

            recipients = await self._fetch_recipients(config.target)

            async with AsyncSessionLocal() as session:
                broadcast = await session.get(BroadcastHistory, broadcast_id)
                if not broadcast:
                    logger.error("Запись рассылки %s удалена до запуска", broadcast_id)
                    return

                broadcast.total_count = len(recipients)
                await session.commit()

            if cancel_event.is_set():
                await self._mark_cancelled(broadcast_id, sent_count, failed_count)
                return

            if not recipients:
                logger.info("Рассылка %s: получатели не найдены", broadcast_id)
                await self._mark_finished(broadcast_id, sent_count, failed_count, cancelled=False)
                return

            keyboard = self._build_keyboard(config.selected_buttons)

            # Ограничение на количество одновременных отправок
            semaphore = asyncio.Semaphore(20)

            async def send_single_message(user):
                """Отправляет одно сообщение с семафором ограничения"""
                async with semaphore:
                    if cancel_event.is_set():
                        return False

                    telegram_id = getattr(user, "telegram_id", None)
                    if telegram_id is None:
                        return False

                    try:
                        await self._deliver_message(telegram_id, config, keyboard)
                        return True
                    except Exception as exc:  # noqa: BLE001
                        logger.error(
                            "Ошибка отправки рассылки %s пользователю %s: %s",
                            broadcast_id,
                            telegram_id,
                            exc,
                        )
                        return False

            # Отправляем сообщения пакетами для эффективности
            batch_size = 100
            for i in range(0, len(recipients), batch_size):
                if cancel_event.is_set():
                    await self._mark_cancelled(broadcast_id, sent_count, failed_count)
                    return

                batch = recipients[i:i + batch_size]
                tasks = [send_single_message(user) for user in batch]
                results = await asyncio.gather(*tasks, return_exceptions=True)

                for result in results:
                    if result is True:
                        sent_count += 1
                    else:
                        failed_count += 1

                # Небольшая задержка между пакетами для снижения нагрузки на API
                await asyncio.sleep(0.1)

            await self._mark_finished(broadcast_id, sent_count, failed_count, cancelled=False)

        except asyncio.CancelledError:
            await self._mark_cancelled(broadcast_id, sent_count, failed_count)
            raise
        except Exception as exc:  # noqa: BLE001
            logger.exception("Критическая ошибка при выполнении рассылки %s: %s", broadcast_id, exc)
            await self._mark_failed(broadcast_id, sent_count, failed_count)

    async def _fetch_recipients(self, target: str):
        async with AsyncSessionLocal() as session:
            if target.startswith("custom_"):
                criteria = target[len("custom_"):]
                return await get_custom_users(session, criteria)
            return await get_target_users(session, target)

    def _build_keyboard(self, selected_buttons: Optional[list[str]]) -> Optional[InlineKeyboardMarkup]:
        if selected_buttons is None:
            selected_buttons = []
        return create_broadcast_keyboard(selected_buttons)