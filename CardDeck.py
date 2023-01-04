from enum import Enum
import random

random.seed(1)

class Colour(Enum):
    RED = (255, 0, 0)
    BLACK = (0, 0, 0)
class Suit(Enum):
    CLUBS = 1
    SPADES = 2
    DIAMONDS = 3
    HEARTS = 4

class Card:
    def __init__(self, colour, suit, value, card_width, card_height, card_colour) -> None:
        # Defining and unchanging features of a card
        self.characteristics = (value, suit, colour)
        # Broader and generally mutable features of a card
        self.attributes = {"Position": (0, 0), "SideLengths": (card_width, card_height), "Colour": card_colour}

        self.hidden = True

    def getCharacteristics(self):
        return self.characteristics
    def getAttributes(self):
        return self.attributes
    def setPosition(self, position):
        self.attributes["Position"] = position

    def getHidden(self):
        return self.hidden
    def reveal(self):
        self.hidden = False
    def hide(self):
        self.hidden = True

    def collideWithPoint(self, point):
        x1, y1 = point
        x2, y2 = self.getAttributes()["Position"]
        width, height = self.getAttributes()["SideLengths"]
        return x2 < x1 and x2 + width > x1 and y2 < y1 and y2 + height > y1
    
    def computeVertices(self) -> list[tuple[float, float]]:
        """ Returns a list of vertices of the card as x, y tuples"""
        x, y = self.getAttributes()["Position"]
        width, height = self.getAttributes()["SideLengths"]
        return [
            (x, y),
            (x, y + height),
            (x + width, y + height),
            (x + width, y)
        ]
    
    def getRenderValue(self, value) -> str:
        card_val = ""
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
        return card_val

    def render(self, pygame, screen, font, position) -> None:
        """ Renders the card, icons, and numbers on the screen """
        self.setPosition(position)
        border_colour = (0, 0, 0)
        value, suit, colour = self.getCharacteristics()
        text_colour = suit.value
        vertices = self.computeVertices()
        # Rendering of the card
        pygame.draw.polygon(screen, self.getAttributes()["Colour"], vertices)
        pygame.draw.lines(screen, border_colour, True, vertices)
        # Rendering of the suit and number
        if not self.getHidden():
            text_surface = font.render(colour.name[0] + " " + self.getRenderValue(value), False, text_colour)
            screen.blit(text_surface, position)


class Deck:
    def __init__(self, card_width, card_height, card_colour) -> None:
        cards = []
        suits = [Suit.CLUBS, Suit.SPADES, Suit.DIAMONDS, Suit.HEARTS]
        for sui in suits:
            if sui in [Suit.CLUBS, Suit.SPADES]:
                col = Colour.BLACK
            else:
                col = Colour.RED
            for i in range(1, 14):
                cards.append(Card(col, sui, i, card_width, card_height, card_colour))
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