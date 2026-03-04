function newStudent(name, age) {
  return {
    name: name,
    age,
    averageScore: 0,
  };
}

const student = newStudent("Григорий", 152, 3);
console.log(student);
