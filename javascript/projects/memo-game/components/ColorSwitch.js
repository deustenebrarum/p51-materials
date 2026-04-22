export class ColorSwitch {
  constructor(element, colors, initialColorIndex) {
    this._element = element;
    this._colors = colors;
    this.setColor(initialColorIndex);
    this.addClickHandler();
  }

  reset() {
    this.setColor(0);
  }

  setColor(index) {
    if (this._colorIndex < 0 || this._colorIndex > this._colors.length) {
      throw new Error("colorIndex is out of colors boundaries");
    }
    this._colorIndex = index;
    this._element.style.backgroundColor = this._colors[this._colorIndex];
  }

  addClickHandler() {
    this._element.addEventListener("click", () => {
      this.setColor((this._colorIndex + 1) % this._colors.length);
    });
  }

  getElement() {
    return this._element;
  }
}

// const backgroundColorList = ["red", "blue", "green"];
// function createColorSwitcher(tag) {
//   const element = document.createElement(tag);
//   let colorIndex = 0;
//   element.addEventListener("click", () => {
//     colorIndex++;
//     if (this.colorIndex >= backgroundColorList.length) {
//       this.colorIndex = 0;
//     }
//     element.style.backgroundColor = ColorSwitcher.backgroundColorList[i];
//   });
// }
