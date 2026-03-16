// Находим на странице элемент, у которого в HTML прописан класс class="app", и записываем его в "коробку" (переменную) под названием element
const element = document.querySelector(".app");

// Берем этот элемент и меняем текст внутри него на "ABABABABB"
element.textContent = "ABABABABB";

// Меняем внешний вид (стили) этого элемента через JavaScript:
// Устанавливаем выравнивание текста по центру
element.style.textAlign = "center";
// Устанавливаем вертикальное выравнивание (правда, для обычных блоков это не всегда работает само по себе, но команда такая есть)
element.style.verticalAlign = "center";
// Делаем шрифт очень крупным — 64 пикселя
element.style.fontSize = "64px";

// Добавляем "слушатель событий". Мы говорим браузеру: "Следи за этим элементом, и если по нему КЛИКНУТ, выполни код в фигурных скобках"
element.addEventListener("click", (event) => {
  // Ниже закомментирован длинный способ проверки класса:
  // if (element.classList.contains("hello")) { // Если у элемента уже есть класс "hello"
  //   element.classList.remove("hello");      // То удали его
  // } else {                                   // А если нет
  //   element.classList.add("hello");         // То добавь его
  // }

  // А это короткий способ сделать то же самое: toggle (переключатель).
  // Если класс "hello" есть — он его уберет, если нет — добавит.
  element.classList.toggle("hello");
});

// Находим на странице список (например, тег <ul> или <ol>) с классом "list"
const listElement = document.querySelector(".list");

// Генерируем случайное число от 1 до 10. Это будет количество новых пунктов в нашем списке
const itemsCount = Math.floor(1 + Math.random() * 10);

// Запускаем цикл: он сработает столько раз, сколько выпало в itemsCount
for (let i = 0; i < itemsCount; i++) {
  // Создаем в памяти браузера новый пустой элемент списка (тег <li>)
  const itemElement = document.createElement("li");

  // Вставляем внутрь этого созданного элемента случайное число от 0 до 99
  itemElement.textContent = Math.floor(Math.random() * 100);

  // Добавляем этот новенький <li> внутрь нашего списка listElement, чтобы он появился на экране
  listElement.appendChild(itemElement);
}

// Находим на странице ссылку (тег <a>) с классом "link"
const linkElement = document.querySelector(".link");

// Меняем у этой ссылки адрес (атрибут href) на "https://google.com"
linkElement.setAttribute("href", "https://google.com");

/* 
  Ниже закомментирован блок с анимацией. 
  Он заставляет элемент плавно ехать вниз и добавлять буквы "А" каждые полсекунды.
  Это сделано через интервалы (таймеры).
*/
// (() => {
//   let top = 0;
//   let interval1 = setInterval(() => {
//     top++;
//     element.style.marginTop = `${top / 10}vh`; // Двигаем элемент вниз
//     if (top > 900) clearInterval(interval1); // Когда доедет до низа — останавливаем
//   }, 10);
//   let interval2 = setInterval(() => {
//     if (element.textContent.length > 20) {
//       clearInterval(interval2); // Если текст стал длиннее 20 символов — останавливаем
//     }
//     element.textContent += "A"; // Дописываем букву "А" в конец
//   }, 500);
// })();
