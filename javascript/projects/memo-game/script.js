"use strict";

import { GameContainer } from "./components/GameContainer.js";

const gameElement = document.querySelector(".game");
const game = new GameContainer(gameElement, 5, 4, 2);
game.initialize();
game.appendDefaultChildren();
