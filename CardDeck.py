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
        self.hidden = True
    def reveal(self):
        self.hidden = False
    def hide(self):
        self.hidden = True

    def getColour(self):
        return self.colour
    def getSuit(self):
        return self.suit
    def getValue(self):
        return self.value
    def getHidden(self):
        return self.hidden
        
    def __str__(self) -> str:
        if self.hidden == False:
            value = self.getValue()
            if value == 1:
                card_val = "A"
            elif value <= 10:
                card_val = str(value)
            elif value == 11:
                card_val = "J"
            elif value == 12:
                card_val = "Q"
            elif value == 13:
                card_val = "K"
            return self.getColour().name[0] + " " + self.getSuit().name[0] + " " + card_val
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
    def getCards(self):
        return self.cards
        
    def __str__(self) -> str:
        deck_str = ""
        for card in self.cards:
            deck_str += str(card) + "\n"
        return deck_str

    def hideCards(self):
        for card in self.getCards():
            card.hide()
    def shuffle(self):
        """ Randomizes the order of the contained card classes """
        random.shuffle(self.cards)