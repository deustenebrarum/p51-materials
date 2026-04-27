import { ColorSwitch } from "./ColorSwitch.js";

export class CardElement {
  static className = "CardElement";

  constructor(element, colorWhenHidden, colorWhenShowed) {
    this._element = element;
    this._element.className = CardElement.className;
    this._colorWhenHidden = colorWhenHidden;
    this._colorWhenShowed = colorWhenShowed;
    this._switch = new ColorSwitch(
      this._element,
      [colorWhenHidden, colorWhenShowed],
      0,
    );
    this._guessed = false;
  }

  set guessed(value) {
    this._guessed = value;
  }

  get guessed() {
    return this._guessed;
  }

  isEqual(card) {
    return card._colorWhenShowed === this._colorWhenShowed;
  }

  clone() {
    return new CardElement(
      this._element.cloneNode(true),
      this._colorWhenHidden,
      this._colorWhenShowed,
    );
  }

  show() {
    this._switch.setColor(1);
  }

  hide() {
    this._switch.setColor(0);
  }

  getElement() {
    return this._element;
  }
}
