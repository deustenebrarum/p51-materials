const modal = document.getElementById("modal");
const openBtn = document.querySelector("[data-open-modal]");
const closeBtn = document.querySelector("[data-close-modal]");
const form = modal.querySelector("form");
const employeesList = document.querySelector(".employees-list");

const inputName = form.querySelectorAll("input")[0];
const inputRole = form.querySelectorAll("input")[1];
const inputEmail = form.querySelectorAll("input")[2];

let currentEditCard = null;

function openModal(editCard = null) {
  currentEditCard = editCard;
  if (editCard) {
    modal.querySelector("h2").textContent = "Редактировать сотрудника";
    inputName.value = editCard.querySelector(".name").textContent;
    inputRole.value = editCard.querySelector(".role").textContent;
    inputEmail.value = editCard.querySelector(".contact").textContent;
  } else {
    modal.querySelector("h2").textContent = "Новый сотрудник";
    form.reset();
  }
  modal.classList.add("active");
}

function closeModal() {
  modal.classList.remove("active");
}

// Открытие модального окна для нового сотрудника
openBtn.addEventListener("click", () => openModal(null));

// Закрытие при клике на крестик
closeBtn.addEventListener("click", closeModal);

// Закрытие при клике по фону (за пределами .modal-content)
modal.addEventListener("click", (event) => {
  if (!event.target.closest(".modal-content")) {
    closeModal();
  }
});

// Открытие модального окна для редактирования сотрудника (делегирование)
employeesList.addEventListener("click", (event) => {
  const card = event.target.closest(".card");
  if (card) {
    openModal(card);
  }
});

// Сохранение (добавление или обновление)
form.addEventListener("submit", (event) => {
  event.preventDefault();

  if (
    !inputName.value.trim() ||
    !inputRole.value.trim() ||
    !inputEmail.value.trim()
  ) {
    return;
  }

  if (currentEditCard) {
    // Обновление существующей карточки
    currentEditCard.querySelector(".name").textContent = inputName.value;
    currentEditCard.querySelector(".role").textContent = inputRole.value;
    currentEditCard.querySelector(".contact").textContent = inputEmail.value;
  } else {
    // Создание новой карточки
    const newCard = document.createElement("div");
    newCard.className = "card";
    newCard.setAttribute("data-employee", "");
    newCard.innerHTML = `
          <div class="name">${inputName.value}</div>
          <div class="role">${inputRole.value}</div>
          <div class="contact">${inputEmail.value}</div>
        `;
    employeesList.appendChild(newCard);
  }

  closeModal();
});
