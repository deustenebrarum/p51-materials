export class CounterButton {
  constructor(caption, action) {
    this._element = document.createElement("button");
    this._element.textContent = caption;
    this._element.addEventListener("click", action);
  }

  getElement() {
    return this._element;
  }
}
