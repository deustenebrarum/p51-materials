// function printByOddity(start, end, toPrintEvens) {
//   for (let number = start; number < end; number++) {
//     const isEvenNumber = number % 2 == 0;
//     if (toPrintEvens == isEvenNumber) {
//       console.log(number);
//     }
//   }
// }
function printByOddity(start, end, toPrintEvens = false) {
  const isEvenStart = start % 2 == 0;
  if (!((isEvenStart && toPrintEvens) || (!isEvenStart && !toPrintEvens))) {
    start += 1;
  }
  for (let number = start; number < end; number += 2) {
    console.log(number);
  }
}

printByOddity(1, 10);
printByOddity(1, 10, true);
