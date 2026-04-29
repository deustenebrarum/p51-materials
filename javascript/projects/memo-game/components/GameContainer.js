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
    this._openedCards = [];
    this._maxRemainingTries = triesCount;
    this._remainingTries = 0;
    this._cardElements = [];

    this._element.addEventListener("click", this.onCardClick.bind(this));
    this._triesCounter = document.createElement("p");
    this._triesCounter.className = "tries-counter";
    this._cardsListContainer = document.createElement("div");
    this._cardsListContainer.className = "cards-container";
    this._cardsList = document.createElement("ol");
    this._cardsList.classList.add("cards");
    this._gameOverElement = document.createElement("p");
    this._gameOverElement.classList.add("game-over", "hidden");
    this._gameOverElement.textContent = "Game Over";
    this._restartButton = document.createElement("button");
    this._restartButton.textContent = "Restart";
    this._restartButton.classList.add("restart-button", "hidden");
    this._restartButton.addEventListener("click", this.restart.bind(this));
  }

  appendDefaultChildren() {
    this._element.appendChild(this._triesCounter);
    this.appendCardsChildren();
    this._cardsListContainer.appendChild(this._cardsList);
    this._element.appendChild(this._cardsListContainer);
    this._cardsListContainer.appendChild(this._gameOverElement);
    this._cardsListContainer.appendChild(this._restartButton);
  }

  initialize() {
    this._openedCards = [];
    this._cardElements = this.generateCards();
    this.updateTriesCounter(this._maxRemainingTries);
  }

  restart() {
    this._cardElements.forEach((card) => card.getElement().remove());
    this.initialize();
    this.appendCardsChildren();
    this._gameOverElement.classList.add("hidden");
    this._cardsList.classList.remove("hidden");
    this._restartButton.classList.add("hidden");
  }

  appendCardsChildren() {
    this._cardElements.forEach((card) =>
      this._cardsList.appendChild(card.getElement()),
    );
  }

  updateTriesCounter(remainingTries) {
    this._remainingTries = remainingTries;
    this._triesCounter.textContent = this._remainingTries;
  }

  onCardClick(event) {
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
  }

  _makeGameOver() {
    this._cardsList.classList.add("hidden");
    this._gameOverElement.classList.remove("hidden");
    this._restartButton.classList.remove("hidden");
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
