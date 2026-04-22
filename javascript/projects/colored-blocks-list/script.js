"use strict";

import { ColorSwitch } from "./ColorSwitch.js";

const blocksList = document.querySelector(".blocks-list");
const switchers = [];
const switchersCount = 4 * 4;

for (let i = 0; i < switchersCount; i++) {
  const element = document.createElement("div");
  element.classList.add("colored-block");
  const switcher = new ColorSwitch(
    element,
    ["hsl(0, 95%, 75%)", "hsl(180, 95%, 75%)"],
    Math.floor(Math.random() * 2),
  );
  switchers.push(switcher);
  blocksList.appendChild(switcher.getElement());
}
