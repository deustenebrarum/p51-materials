"use strict";

const [hours, minutes, seconds] = prompt("Input time(HH:mm:ss)")
  .split(":")
  .map(Number);

// const number = +prompt("Input number");
//
// if (number != 0 && number % 2 === 0 || false) {
//   confirm("even");
// } else {
//   alert("odd");
// }

// const age = +prompt("What is your age?");
//
// if (isNaN(age)) {
//   console.log("wrong input");
// } else {
//   if (age < 18) {
//     console.log("You shall not pass");
//   } else {
//     console.log("You're welcome");
//   }
// }
