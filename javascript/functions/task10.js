function isLeap(year) {
  return year % 400 == 0 || (year % 4 == 0 && year % 100 != 0);
}

function formatDate(day, month, year) {
  const dayFormatted = String(day).padStart(2, "0");
  const monthFormatted = String(month).padStart(2, "0");
  const yearFormatted = String(year).padStart(4, "0");
  return `${dayFormatted}.${monthFormatted}.${yearFormatted}`;
}

function getDaysCount(month, year) {
  switch (month) {
    case 2:
      return isLeap(year) ? 29 : 28;
    case 4:
    case 6:
    case 9:
    case 11:
      return 30;
  }
  return 31;
}

function getNextDayFormatted(day, month, year) {
  const monthsPerYear = 12;
  day++;
  if (day > getDaysCount(month, year)) {
    day = 1;
    month++;
  }
  if (month > monthsPerYear) {
    year++;
    month = 1;
  }

  return formatDate(day, month, year);
}

function testGetDaysCount() {
  console.log(getDaysCount(1, 2000) == 31);
  console.log(getDaysCount(2, 2000) == 29);
  console.log(getDaysCount(2, 2001) == 28);
  console.log(getDaysCount(3, 2000) == 31);
  console.log(getDaysCount(4, 2000) == 30);
  console.log(getDaysCount(5, 2000) == 31);
  console.log(getDaysCount(6, 2000) == 30);
  console.log(getDaysCount(7, 2000) == 31);
  console.log(getDaysCount(8, 2000) == 31);
  console.log(getDaysCount(9, 2000) == 30);
  console.log(getDaysCount(10, 2000) == 31);
  console.log(getDaysCount(11, 2000) == 30);
  console.log(getDaysCount(12, 2000) == 31);
  console.log();
}

function testGetNextDayFormatted() {
  console.log(getNextDayFormatted(6, 6, 2000) == "07.06.2000");
  console.log(getNextDayFormatted(30, 6, 2000) == "01.07.2000");
  console.log(getNextDayFormatted(31, 5, 2000) == "01.06.2000");
  console.log(getNextDayFormatted(29, 2, 2000) == "01.03.2000");
  console.log(getNextDayFormatted(28, 2, 2000) == "29.02.2000");
  console.log(getNextDayFormatted(31, 12, 2000) == "01.01.2001");
  console.log(getNextDayFormatted(28, 2, 2001) == "01.03.2001");
}

testGetDaysCount();
testGetNextDayFormatted();
