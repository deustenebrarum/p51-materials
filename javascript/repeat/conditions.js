function isLeap(year) {
  return year % 400 === 0 || (year % 4 === 0 && year % 100 !== 0);
}
const year = 1400;
// Год делится на 400, либо год и делится на 4 и не делится на 100
if (isLeap(year)) {
}
