from blackjack import Blackjack

low_cards = ["2", "3", "4", "5", "6"]
high_cards = ["10", "Jack", "Queen", "King", "Ace"]

advices = {
    "high": "Bet High: The deck is favorable for you.",
    "low": "Bet Low: The deck is unfavorable.",
    "neutral": "Play Normally: The deck is neutral.",
}

results = {
    "player_win": "You win!",
    "player_bust": "You bust! House wins.",
    "house_win": "House wins.",
    "house_bust": "House busts! You win.",
    "tie": "It's a tie.",
}


class Game:
    def __init__(self, num_decks=1):
        """
        Initialize the Game with a specified number of decks.
        :param num_decks: Number of decks used at the table.
        """
        self.num_decks = num_decks
        self.table = Blackjack()
        self.house_hand = 0

    def _update_count(self, card):
        """
        Update the card count based on the dealt card.
        :param card: A card string (e.g., "2 of Hearts").
        """

    def _get_hand_value(self, hand):
        """
        Calculate the total value of a hand.
        Aces count as 11 unless they would cause the hand to bust.
        """

    def _get_advice(self):
        """
        Provide advice based on the current card count.
        :return: A string with advice.
        """

    def deal(self, player):
        """
        Deal two cards to a player and the house, and update the card count.
        Also prints advice based on the card count.
        :param player: The player's identifier.
        """
        cards = self.table.deal(player)
        self.house_hand = cards

    def hit(self, player):
        """
        Perform a hit for the player and update the card count.
        Also prints advice based on the card count.
        :param player: The player's identifier.
        """
        self.table.hit(player)

    def split(self, player):
        """Perform a split for the player."""
        self.table.split(player)

    def fold(self, player):
        """Perform a fold for the player."""
        self.table.fold(player)

    def reveal(self, player):
        """
        Reveal the house's hand and determine the winner.
        :param player: The player's identifier.
        """

    def reset(self):
        """Reset the game state and card count."""

    def run(self):
        """Run the Game and accept user commands."""
        print("Welcome to the Blackjack Game!")
        print("Commands: deal, hit, split, fold, reveal, reset, quit")

        while True:
            command = input("Enter command: ").strip().lower()
            if command == "quit":
                print("Exiting the game. Goodbye!")
                break
            elif command in ["deal", "hit", "split", "fold", "reveal"]:
                player = input("Enter player name: ").strip()
                if command == "deal":
                    self.deal(player)
                elif command == "hit":
                    self.hit(player)
                elif command == "split":
                    self.split(player)
                elif command == "fold":
                    self.fold(player)
                elif command == "reveal":
                    self.reveal(player)
            elif command == "reset":
                self.reset()
            else:
                print("Invalid command. Try again.")
