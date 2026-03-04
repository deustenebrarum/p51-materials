function isPrime(number) {
  for (let i = 2; i <= number / 2; i++) {
    if (number % i === 0) {
      return false;
    }
  }
  return true;
}
// Выведите на экран все числа от 1 до 8

// Пусть изначально i = 1, Пока i < 8 выводить на экран i, увеличивать i на 1
let i = 1;
while (i <= 8) {
  console.log(i);
  i++;
}

const number = 8;
// Выведите на экран все простые числа от 1 до number

// Можно узнать, что число простое.
// Для i = 1; пока i < number; увечивая i на 1 после итерации;
// на каждой итерации, если i простое, то выводить i
for (let i = 1; i < number; i++) {
  if (isPrime(i)) {
    console.log(i);
  }
}
