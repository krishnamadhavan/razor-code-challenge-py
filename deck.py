import random


class Deck:
    SUITS = ["Hearts", "Diamonds", "Clubs", "Spades"]
    RANKS = [
        "2",
        "3",
        "4",
        "5",
        "6",
        "7",
        "8",
        "9",
        "10",
        "Jack",
        "Queen",
        "King",
        "Ace",
    ]

    def __init__(self):
        """Initialize the deck with a full set of 52 cards."""
        self.cards = [
            f"{rank} of {suit}" for suit in self.SUITS for rank in self.RANKS
        ]
        self.shuffle()

    def shuffle(self):
        """Shuffle the deck."""
        random.shuffle(self.cards)
        # self.cards.append(self.cards.pop(0))

    def draw(self):
        """
        Draw a card from the deck.

        Raises:
            IndexError: If no cards are left in the deck.
        """
        if len(self.cards) == 0:
            raise IndexError("No cards are left in the deck.")

        return self.cards.pop()

    def reset(self):
        """Reset the deck to the original state and shuffle it."""
        self.__init__()

    def remaining_cards(self):
        """Return the number of cards left in the deck."""
        return len(self.cards)

    def __str__(self):
        """Return a string representation of the remaining cards in the deck."""
        return f"Deck with {len(self.cards)} cards remaining."
