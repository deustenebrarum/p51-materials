const obj = {
  1: 5,
  8: 9,
  hello: "world",
};

console.log(obj[8]);
console.log(obj[5]);
console.log(obj["hello"]);
console.log(obj.hello);

const taskProto = {
  _lastNumber: 1,
  number: undefined,
  title: undefined,
  description: undefined,
  _isDone: false,
  complete() {
    this._isDone = true;
  },
  log() {
    console.log(
      this.number,
      this.title,
      this.description,
      this._isDone ? "Done" : "Not done",
    );
    console.log(this);
  },
};
console.log(taskProto);
taskProto.complete();

function newTask(title, description) {
  const task = Object.assign({}, taskProto);

  task.number = taskProto._lastNumber;
  taskProto._lastNumber++;
  task.title = title;
  task.description = description;

  return task;
}

function Task(title, description) {
  // const task = Object.assign({}, taskProto);

  this.number = taskProto._lastNumber;
  taskProto._lastNumber++;
  this.title = title;
  this.description = description;

  // return task;
}
Object.setPrototypeOf(Task.prototype, taskProto);

const task2 = {};
task2.__proto__ = taskProto;

task2.log();
task2.complete();
task2.log();
