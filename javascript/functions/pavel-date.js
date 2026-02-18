"use strict";
const prompt = require('prompt-sync')();

//Проверка на високосный год
function isLeap (year) {
    return (year%400 === 0 || (year%4 === 0 && year%100 !== 0));
}

//Получение количества дней в месяце
function getDaysCountInMonth(month, year) {
    switch (month) {
        case 2: return isLeap(year) ? 29 : 28;
        case 4:
        case 6:
        case 9:
        case 11: return 30;
    }
    return 31;
}

//Запрос ввода года
function input_year() {
    let year = +prompt("Введите год (не более 2026): ");
    while (year < 1 || year > 2026 || year == isNaN(year)) {
        console.log("Неверно указан год, повторите ввод");
        year = +prompt("Введите год: ");
    }
    return year;    
}

//Запрос ввода месяца
function input_month() {
    let month = +prompt("Введите меясяц (от 1 до 12): ");
    
    while (month < 1 || month > 12 || month == isNaN(month) ) {
        console.log("Неверно указан месяц, повторите ввод");
        month = +prompt("Введите меясяц: ");
    }

    return month;
}

//Запрос ввода дня с проверкой на високосный год
function input_day(month, year) {
    let day = +prompt("Введите день: ");
    while (day < 1 || day > getDaysCountInMonth(month, year) || day == isNaN(day)) {

        console.log(`Неверно указан день, повторите ввод, в месяце ${getDaysCountInMonth(month, year)}`);
        day = +prompt("Введите день: ");
    }
    return day;    
}

//Подсчитывание количества дней от 01.01.0000
function getDaysCountToDate(day, month, year) {
    let temp = 0;
    for (let i = 0; i < year; i++) {
        if (isLeap(i)) {
            temp += 366;
        } else {
            temp += 365;
        }
    }

    for (let j = 1; j <= month; j++) {
        if (j == 4 || j == 6 || j == 9 || j == 11) {
            temp += 30;
        } else if (j == 2) {
            temp += 28;
        } else {
            temp += 31;
        }
    }

    // if (isLeap(year)) {
    //     temp++;
    // }
    temp += day;
    return temp;
}

//Ввод данных
const year1 = input_year();
const month1 = input_month()
const day1 = input_day(month1, year1);

const year2 = input_year();
const month2 = input_month()
const day2 = input_day(month2, year2);

//Разница дней между датами
function difference_between_dates(day1, month1, year1, day2, month2, year2) {
    let DaysCountFirstDate =  getDaysCountToDate(day1, month1,year1);
    let DaysCountSecondDate = getDaysCountToDate(day2, month2,year2);

    return DaysCountSecondDate - DaysCountFirstDate;
}

console.log(difference_between_dates(day1, month1, year1, day2, month2, year2));