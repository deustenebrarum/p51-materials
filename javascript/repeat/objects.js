// function newStudent(fullName, age) {
//   return {
//     name: fullName,
//     age,
//     averageScore: 0,
//     getClassNumber() {
//       return Math.min(11, age - 7);
//     }
//   };
// }
// function declaration - объявление функции
function Student(fullName, age) {
  // this = {}
  this.name = fullName;
  this.age = age;
  this.averageScore = 0;
  // function expression - функция-выражение
  // this.getClassNumber = function () {
  //   // this =
  //   return Math.min(11, this.age - 7);
  // };
  // return this
}

Student.prototype.getClassNumber = function () {
  // this =
  return Math.min(11, this.age - 7);
};
Student.prototype.a = 10;
Student.prototype.toString = function () {
  // this =
  return "hello";
};

const student1 = new Student("Григорий", 17);
const student2 = new Student("Алёша", 14);
student2.a = 5;
console.log(student1.a);
