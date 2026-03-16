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
  this.name = fullName;
  this.age = age;
  this.averageScore = 0;
}

Student.prototype.getClassNumber = function () {
  return Math.min(11, this.age - 7);
};

Student.prototype.printInfo = function () {
  console.log(this.name, this.age, this.averageScore);
};

const student1 = new Student("Григорий", 17);
const student2 = new Student("Гоша", 14);
student2.printInfo();
