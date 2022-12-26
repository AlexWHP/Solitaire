from enum import Enum
import random

random.seed(1)

class Colour(Enum):
    RED = 1
    BLACK = 2
class Suit(Enum):
    CLUBS = 1
    SPADES = 2
    DIAMONDS = 3
    HEARTS = 4

class Card:
    def __init__(self, colour, suit, value) -> None:
        self.colour = colour
        self.suit = suit
        self.value = value
        self.hidden = False
        self.pile = None
    def changePile(self, new_pile) -> None:
        """  Called if a card is succesfully changed from one pile to another """
        self.pile = new_pile
    def __str__(self) -> str:
        if self.hidden == False:
            if self.value <= 10:
                card_val = str(self.value)
            elif self.value == 11:
                card_val = "J"
            elif self.value == 12:
                card_val = "Q"
            elif self.value == 13:
                card_val = "K"
            return self.colour.name + " " + self.suit.name[0] + " " + card_val
        else:
            return "Card is hidden"

class Deck:
    def __init__(self) -> None:
        cards = []
        suits = [Suit.CLUBS, Suit.SPADES, Suit.DIAMONDS, Suit.HEARTS]
        for sui in suits:
            if sui in [Suit.CLUBS, Suit.SPADES]:
                col = Colour.BLACK
            else:
                col = Colour.RED
            for i in range(1, 14):
                cards.append(Card(col, sui, i))
        self.cards = cards

    def getCard(self, index) -> Card:
        return self.cards[index]

    def __str__(self) -> str:
        deck_str = ""
        for card in self.cards:
            deck_str += str(card) + "\n"
        return deck_str

    def shuffle(self):
        """ Randomizes the order of the contained card classes """
        random.shuffle(self.cards)