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
        deck = []
        suits = [Suit.CLUBS, Suit.SPADES, Suit.DIAMONDS, Suit.HEARTS]
        for sui in suits:
            if sui in [Suit.CLUBS, Suit.SPADES]:
                col = Colour.BLACK
            else:
                col = Colour.RED
            for i in range(1, 14):
                deck.append(Card(col, sui, i))
        self.deck = deck

    def __str__(self) -> str:
        deck_str = ""
        for card in self.deck:
            deck_str += str(card) + "\n"
        return deck_str

    def shuffle(self):
        """ Randomizes the order of the contained card classes """
        random.shuffle(self.deck)

class Foundations:
    """ Initially empty but aimed to be filled with a single ordered suit """
    def __init__(self) -> None:
        pass

class Tableau:
    """ Workspace to help transfer cards to the Tableau """
    def __init__(self) -> None:
        pass
    def move():
        pass
    
class Stock:
    """ Rotating deck of cards to be pulled into the Foundations or Tableau"""
    def __init__(self) -> None:
        pass

class Solitaire:
    def __init__(self) -> None:
        self.deck = Deck()
        self.foundations = [Foundations()]*4
        self.tableaus = [Tableau()]*7
        self.stock = Stock()
    def createGame(self):
        deck_index = 0
        for tabs in self.tableaus:
            tabs.addCard(self.deck.getCard(deck_index))
            deck_index += 1


d = Deck()
d.shuffle()
print(d)