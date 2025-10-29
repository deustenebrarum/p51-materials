class Card:
    CLUBS = "Clubs"  # трефы
    DIAMONDS = "Diamonds"  # буби
    HEARTS = "Hearts"  # черви
    SPADES = "Spades"  # пики

    def __init__(self, suit, rank: int):
        self._suit = suit
        self._rank = rank

    @property
    def suit(self):
        return self._suit

    @property
    def rank(self):
        return self._rank

    def is_superior(self, other: 'Card'):
        return (
            self.suit == other.suit and
            self.rank > other.rank
        )

    def __eq__(self, other: 'Card'):
        return (
            self.suit == other.suit and
            self.rank == other.rank
        )

    def __str__(self):
        return f"{self.rank} of {self.suit}"


card1 = Card(Card.CLUBS, 10)
print(card1.suit)
