import itertools, random

class Deck:
    def __init__(self):
        # Create a deck of the top 5 cards of each suit.
        self.cards = list(itertools.product(range(10,14),['s','h','d','c']))
        # Shuffle.
        random.shuffle(self.cards)

    # Convert the numeric rank to the card's face value.
    def rank_to_face(self, rank):
        switcher = {
            10: "T",
            11: "J",
            12: "Q",
            13: "K",
            14: "A",
        }
        return switcher.get(rank)

    # Draw the desired number of cards off the top
    def draw(self, count):
        drawn_cards = {}
        for i in range(count):
            drawn_cards[i] = [self.rank_to_face(self.cards[i][0]), self.cards[i][1]]
        return drawn_cards
            