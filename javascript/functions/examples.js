function getExclamated(text) {
  if (!text) {
    return text;
  }
  if (text === "") {
    return "";
  }
  return text + "!";
}

function exclamate(text) {
  console.log(getExclamated(text));
}

exclamate("Hello");
console.log(getExclamated("Goodbye") === "Goodbye!");
console.log(getExclamated("") === "");
console.log(getExclamated(null) === null);
console.log(typeof getExclamated(undefined) === 'undefined');

// Переиспользуемость + универсальность - можно использовать много раз с рызными АРГУМЕНТАМИ,
//   при изменении - код меняется везде
// Читаемость, потому что название понятнее кода
// Тестируемость
// всё вместе = Модульность, легко встраивать, искать или переносить
