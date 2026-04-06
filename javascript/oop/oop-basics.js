// Инкапсуляция - объединение логики, требуемой для решения
//   определённых задач внутри объектов
class Animal {
  constructor(name, age) {
    this.name = name;
    this.age = age;
  }

  run() {
    console.log(`${this.name} бежит уже ${this.age} лет`);
    this.age++;
  }
}

// Наследования - возможность сделать так, чтобы один тип объектов(класс)
//  имел все возможности(являлся) другого объекта
class Bird extends Animal {
  fly() {
    console.log(`${this.name} летит уже ${this.age} лет`);
  }
}

const animal = new Animal("Kesha", 4);
animal.run();
animal.fly();

class Person {
  constructor(name) {
    this.name = name;
  }

  run() {}
}

/**
 * @param {Animal} animal
 */
function test(animal) {
  for (let i = 0; i < 3; i++) animal.run();
  animal.name = "Бешеный " + animal.name;
}
