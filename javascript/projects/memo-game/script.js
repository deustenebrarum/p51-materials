"use strict";

import { GameContainer } from "./components/GameContainer";

const gameElement = document.querySelector(".game");
const game = new GameContainer(gameElement, 5, 4);
game.initialize();
