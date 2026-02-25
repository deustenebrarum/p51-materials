function isLeap(year) {
  return year % 4 === 0 && (year % 100 !== 0 || year % 400 === 0);
}

function getDaysFromMonthNumber(monthNumber, year) {
  switch (monthNumber) {
    case 1:
    case 3:
    case 5:
    case 7:
    case 8:
    case 10:
    case 12:
      return 31;
    case 4:
    case 6:
    case 9:
    case 11:
      return 30;
    case 2:
      return isLeap(year) ? 29 : 28;
  }

  return null;
}

function countLeapYearsBy(year) {
  let count = 0;
  for (let i = 4; i < year; i += 4) {
    if (isLeap(i)) {
      count++;
    }
  }
  return count;
}

function getAsDays(day, month, year) {
  const daysPerYear = 365;
  let daysCount = 365 * year;

  daysCount += countLeapYearsBy(year);

  for (let i = 1; i < month; i++) {
    daysCount += getDaysFromMonthNumber(i, year) ?? 0;
  }

  daysCount += day;

  return daysCount;
}

function getDifferenceBetweenDates(day1, month1, year1, day2, month2, year2) {
  return getAsDays(day2, month2, year2) - getAsDays(day1, month1, year1);
}

console.log(getDifferenceBetweenDates(1, 1, 2000, 1, 1, 2000), 0);
console.log(getDifferenceBetweenDates(1, 2, 2020, 1, 3, 2020), 29);
console.log(getDifferenceBetweenDates(1, 1, 2000, 1, 1, 2001), 366);
console.log(getDifferenceBetweenDates(1, 1, 2000, 1, 1, 2005), 365 * 5 + 2);
