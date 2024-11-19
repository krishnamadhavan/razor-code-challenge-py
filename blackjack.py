from deck import Deck


class Blackjack(Deck):
    def __init__(self, num_decks=1):
        """
        Initialize the Blackjack table with a specified number of decks.
        :param num_decks: Number of decks to use at the table.
        """
        super().__init__()
        self.num_decks = num_decks
        self.active_hands = dict()

    def reset(self):
        """Reset the table by shuffling all decks together and clearing active hands."""
        self.__init__()

    def deal(self, player):
        """
        Deal two cards to a player.
        :param player: The player's identifier (e.g., a name or number).
        """
        cards = [self.draw(), self.draw()]
        self.active_hands[player] = cards
        return cards

    def hit(self, player):
        """
        Add a card to the player's hand.
        :param player: The player's identifier.
        """
        self.active_hands[player].append(self.draw())

    def split(self, player):
        """
        Split a player's hand into two if the first two cards are of the same rank.
        :param player: The player's identifier.
        """
        cards = self.active_hands[player]
        rank_1, rank_2 = cards[0].split(" ")[0], cards[1].split(" ")[0]

        if rank_1 == rank_2:
            self.active_hands[f"{player}_split"] = [cards.pop(0)]
            self.hit(f"{player}_split")
            self.hit(player)

    def fold(self, player):
        """
        Fold the player's hand, removing them from the active hands.
        :param player: The player's identifier.
        """
        self.active_hands.pop(player, None)
