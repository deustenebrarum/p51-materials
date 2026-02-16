// function min(a, b, c, d, e) {
//   let currentMin = a;
//   if (b < currentMin) {
//     currentMin = b;
//   }
//   if (c < currentMin) {
//     currentMin = c;
//   }
//   if (d < currentMin) {
//     currentMin = d;
//   }
//   if (e < currentMin) {
//     currentMin = e;
//   }
//   return currentMin;
// }

// function min(...numbers) {
//   let currentMin = numbers[0];
//   for (let i = 0; i < numbers.length; i++) {
//     if (numbers[i] < currentMin) {
//       currentMin = numbers[i];
//     }
//   }
//   return currentMin;
// }
//

function min() {
  let currentMin = arguments[0];
  for (let i = 0; i < arguments.length; i++) {
    if (arguments[i] < currentMin) {
      currentMin = arguments[i];
    }
  }
  return currentMin;
}
console.log(min(1));
console.log(min(2, 1));
console.log(min(2, 1, 3));
console.log(min(2, 1, 3, 4));
console.log(min(2, 5, 3, 4, 1));
