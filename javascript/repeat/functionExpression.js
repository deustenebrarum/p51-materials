function isProductOf2And7(number) {
  return number % 2 == 0 && number % 7 == 0;
}
// const isProductOf9 = function (number) {
//   return number % 9 == 0;
// };

function test(start, end, isValid) {
  for (let i = start; i < end; i++) {
    if (isValid(i)) {
      console.log(i);
    }
  }
}
// test(1, 50, isProductOf9);
test(1, 50, (number) => number % 9 == 0);

const a = [1, 6, 4, 3, 2];
const b = a.filter((x) => x % 2 == 0);
b.sort((x, y) => y - x);
console.log(b);
