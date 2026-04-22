export class CounterController {
  constructor(baseCount = 0) {
    this._count = baseCount;
  }

  increment() {
    this._count++;
  }

  decrement() {
    this._count--;
  }

  get count() {
    return this._count;
  }
}
