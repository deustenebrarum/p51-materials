// константа
const a = { p1: 1, p2: 2 };
a.p2 = 3;
// a = 3; ошибка

// области видимости - перекрытие
let bVariable = 3;
if (true) {
  const b = 1;
  console.log(b); // 1
}
console.log(bVariable); // 3

// области видимости - перезапись существующей переменной
let c = 3;
if (true) {
  c = 1;
  console.log(c); // 1
}
console.log(c); // 1

// обмен значениями переменных - любой язык
let var1 = 1;
let var2 = 5;

const temp = var1;
var1 = var2;
var2 = temp;

console.log(var1, var2); // 5 1

// другим способом
[var1, var2] = [var2, var1];
console.log(var1, var2); // 1 5
