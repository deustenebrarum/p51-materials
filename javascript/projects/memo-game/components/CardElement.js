import { ColorSwitch } from "./ColorSwitch";

export class CardElement {
  constructor(element, colorWhenHidden, colorWhenShowed) {
    this._element = element;
    this._switch = new ColorSwitch(
      this._element,
      [colorWhenHidden, colorWhenShowed],
      0,
    );
  }

  clone() {}

  show() {}

  hide() {}

  getElement() {
    return this._element;
  }
}
