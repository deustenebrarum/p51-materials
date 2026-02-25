// const o = {
//   x: 2,
//   test() {
//     console.log(x);
//   },
// };
//
// function f(b) {
//   b.test();
// }
//
// o.test();
// f(o);
// создаём функцию с названием findCandidate - найти кандидата
function findCandidate() {
  // создаём возвращаем объект с кандидатом
  return {
    // задаём имя - Илья
    name: "Ilya",
    // задаём год первого устройства - 1999
    firstEmployedYear: 1999,
    // создаём метод(функции внутри объекта) для получения опыта работы
    getExperience() {
      // this = candidate
      // получаем сегодняшний год, вычитаем год первого трудоустройства ЭТОГО объекта,
      // возвращаем результат
      return new Date().getFullYear() - this.firstEmployedYear;
    },
  };
}

// создаём функцию, которая проверяет, что кандидат проходит требования по стажу
// принимаем кандидата и минимальный стаж
function doPassRequirements(candidate, minExperience) {
  // возвращаем больше ли стаж кандидата, чем требуемый минимально
  return candidate.getExperience() >= minExperience;
}

// печатаем ответ
console.log(
  // получаем ответ на вопрос, проходит ли найденный кандидат
  // минимальный порог в 30 лет опыта
  doPassRequirements(
    // получаем кандидата из функции findCandidate
    findCandidate(),
    30,
  ),
);
