const prompt = require("prompt-sync")();

function task1() {
  const number = +prompt("number:");

  if (number > 0) {
    console.log("positive");
    console.log("im so happy");
  } else if (number < 0) {
    console.log("negative");
  } else {
    console.log("zero");
  }
}

function task2() {
  const age = +prompt("number:");
  if (age <= 0 || age >= 120) {
    console.log("Access denied");
  }
}

function task3() {
  let number = +prompt("number: ");
  if (age < 0) {
    number = -number;
  }
  console.log(number);
}

function task3() {
  let x = +prompt("x: ");
  let y = +prompt("y: ");
  //  y
  // 4|1
  // ---x
  // 3|2
  if (x > 0 && y > 0) {
    console.log("First quadrant");
  } else if (x > 0 && y < 0) {
    console.log("Second quadrant");
  } else if (x < 0 && y > 0) {
    console.log("Third quadrant");
  } else if (x < 0 && y < 0) {
    console.log("Fourth quadrant");
  } else {
    console.log("Axis");
  }
}

const monthNumber = +prompt("Month number: ");
let month;
switch (monthNumber) {
  case 1:
    month = "Январь";
    break;
  case 2:
    month = "Февраль";
    break;
  case 3:
    month = "Март";
    break;
  case 4:
    month = "Апрель";
    break;
  case 5:
    month = "Май";
    break;
  case 6:
    month = "Июнь";
    break;
  case 7:
    month = "Июль";
    break;
  case 8:
    month = "Август";
    break;
  case 9:
    month = "Сентябрь";
    break;
  case 10:
    month = "Октябрь";
    break;
  case 11:
    month = "Ноябрь";
    break;
  case 12:
    month = "Декабрь";
    break;
  default:
    month = "Неверный месяц";
}

console.log(month);
