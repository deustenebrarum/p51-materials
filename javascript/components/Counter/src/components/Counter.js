import { CounterButton } from "./CounterButton.js";
import { CounterController } from "./CounterController.js";

export class Counter {
  constructor() {
    this._controller = new CounterController();
    this._element = this._createRoot(this._controller);
    this._element.appendChild(
      new CounterButton("+", () => {
        this._controller.increment();
        this._element.querySelector("p").textContent = this._controller.count;
      }).getElement(),
    );
    this._element.appendChild(
      new CounterButton("-", () => {
        this._controller.decrement();
        this._element.querySelector("p").textContent = this._controller.count;
      }).getElement(),
    );
  }

  _createRoot(counterController) {
    const root = document.createElement("div");
    const textContainer = document.createElement("p");
    root.style.textAlign = "center";
    textContainer.textContent = `${counterController.count}`;
    // При клике увеличивать текст на единицу.
    textContainer.addEventListener("click", () => {
      counterController.increment();
      textContainer.textContent = `${counterController.count}`;
    });
    root.appendChild(textContainer);
    return root;
  }

  getElement() {
    return this._element;
  }
}
