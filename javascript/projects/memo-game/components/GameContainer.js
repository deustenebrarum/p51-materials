import { CardElement } from "./CardElement.js";

export class GameContainer {
  constructor(element, rows, cols, triesCount) {
    this._maxOpenedCount = 2;
    this._element = element;
    if ((rows * cols) % this._maxOpenedCount != 0) {
      throw new Error("Game can't have odd amount of cards");
    }
    this._rows = rows;
    this._cols = cols;
    this._cardElements = this.generateCards();
    this._triesCounter = document.createElement("p");
    this._triesCounter.className = "tries-counter";
    this.updateTriesCounter(triesCount);
    this._openedCards = [];
  }

  initialize() {
    this._element.appendChild(this._triesCounter);

    const cardsListContainer = document.createElement("div");
    cardsListContainer.className = "cards-container";
    const cardsList = document.createElement("ol");
    cardsList.classList.add("cards");
    this._cardElements.forEach((card) =>
      cardsList.appendChild(card.getElement()),
    );
    cardsListContainer.appendChild(cardsList);
    this._element.appendChild(cardsListContainer);
    this.addCardClickListener();
  }

  updateTriesCounter(remainingTries) {
    this._remainingTries = remainingTries;
    this._triesCounter.textContent = this._remainingTries;
  }

  addCardClickListener() {
    this._element.addEventListener("click", (event) => {
      const cardHTMLElement = event.target.closest(`.${CardElement.className}`);
      if (!cardHTMLElement) {
        return;
      }

      const selectedCard = this._cardElements.find(
        (cardElement) => cardElement.getElement() == cardHTMLElement,
      );

      if (selectedCard.guessed) return;

      if (this._openedCards.length >= this._maxOpenedCount) {
        const isEqualToFirst = (card) => card.isEqual(this._openedCards[0]);
        if (this._openedCards.every(isEqualToFirst)) {
          this._openedCards.forEach((card) => (card.guessed = true));
        } else {
          this.updateTriesCounter(this._remainingTries - 1);
          if (this._remainingTries <= 0) {
            this._makeGameOver();
          }
          this._openedCards.forEach((card) => card.hide());
        }
        this._openedCards = [];
      } else if (this._openedCards.at(-1) == selectedCard) {
        return;
      }

      this._openedCards.push(selectedCard);
      selectedCard.show();
    });
  }

  _makeGameOver() {
    const cardsList = this._element.querySelector(".cards");
    const parent = cardsList.parentElement;
    cardsList.remove();
    const gameOverElement = document.createElement("p");
    gameOverElement.className = "game-over";
    gameOverElement.textContent = "Game Over";
    parent.appendChild(gameOverElement);
  }

  getElement() {
    return this._element;
  }

  static _generatePalette(count) {
    const step = 360 / count;
    let currentHue = 32;
    let isEven = false;
    return new Array(count).fill(null).map(() => {
      const result = `hsl(${Math.floor(currentHue % 360)}, 80%, ${isEven ? "60" : "80"}%)`;
      currentHue += step;
      isEven = !isEven;
      return result;
    });
  }

  generateCards() {
    const pairsCount = (this._rows * this._cols) / 2;

    const [hiddenColor, ...cardColors] = GameContainer._generatePalette(
      pairsCount + 1,
    );

    const cardElements = [];

    for (let i = 0; i < pairsCount; i++) {
      const card = new CardElement(
        document.createElement("li"),
        hiddenColor,
        cardColors[i],
      );
      cardElements.push(card);
      cardElements.push(card.clone());
    }

    cardElements.sort((a, b) => Math.random() - 0.5);

    return cardElements;
  }
}
