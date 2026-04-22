import { Counter } from "./components/Counter.js";

class App {
  constructor(element) {
    this._element = element;
    this._element.appendChild(new Counter().getElement());
  }
}
const app = new App(document.getElementById("app"));
