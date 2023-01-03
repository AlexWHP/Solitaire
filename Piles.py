from CardDeck import Card

class Piles:
    def __init__(self) -> None:
        self.stack = []
        self.position = (0, 0)
        self.side_length = (0, 0)
    def resetStack(self):
        self.stack = []
    def getStack(self):
        return self.stack
    def setStack(self, cards):
        self.stack = cards
    def getPosition(self):
        return self.position
    def setPosition(self, position):
        self.position = position
    def getSideLengths(self):
        return self.side_length
    def setSideLengths(self, side_length):
        self.side_length = side_length
    def getTopCard(self):
        """ Returns the top card of the pile """
        if len(self.getStack()) > 0:
            return self.getStack()[-1]
        return None
    def validMove(self):
        """ Determines if a card is able to be added on top of another from the pile """
        raise NotImplementedError
    def addCards(self, cards):
        """ Adds a card to the top of the pile """
        raise NotImplementedError
    def removeCards(self, cards):
        """ Checks if a card can be removed from the pile """
        stack = self.getStack()
        stack = stack[:stack.index(cards[0])]
    def collideWithPoint(self, point) -> bool:
        """ Checks if a point intersects with the pile """
        x1, y1 = point
        x2, y2 = self.getPosition()
        width, height = self.getSideLengths()
        return x2 < x1 and x2 + width > x1 and y2 < y1 and y2 + height > y1
    def collideWithCards(self, point) -> bool:
        """ Checks if a point interacts with the cards within the pile """
        raise NotImplementedError
            
    def render(self, pygame, screen, font, position) -> None:
        raise NotImplementedError

class Foundation(Piles):
    """ Initially empty but aimed to be filled with a single ordered suit """
    def validMove(self, card):
        """ Valid if an ace is moved onto an empty foundation or is the same suit and one value higher than the current top card """
        stack = self.getStack()
        if len(stack) > 0:
            return card.value == 1
        current_card = stack.getTopCard()
        return card.getSuit() != current_card.getSuit() and current_card.getValue() == card.getValue() + 1
    def addCards(self, cards):
        """ Only singular cards can be added onto the foundation piles """
        if len(cards) == 1 and self.validMove(cards[0]):
            self.stack += cards
            return True
        return False
    def render(self, pygame, screen, font, position):
        """ Renders the foundation cards horizontally """
        cards = self.getStack()
        if len(cards) > 0:
            x, y = position
            
            card_width = 80
            card_height = 120
            cards[-1].render(pygame, screen, font, (x, y), (card_width, card_height))
            self.setPosition(position)
            self.setSideLengths((card_width, card_height))
    def collideWithCards(self, point) -> list[Card, Card]:
        """ Checks if a point collides with a point """
        # Searches the stack in reverse and returns the first card hit
        cards = self.getStack()
        for i in range(len(cards)):
            if cards[i].collideWithPoint(point):
                return cards[i:]
        return None

class Tableau(Piles):
    """ Workspace to help transfer cards to the Tableau """
    def validMove(self, add_card):
        """ Valid if the selected card can be placed on top of this card (Others can be assumed valid) """
        current_card = self.getTopCard()
        # The tableau is empty meaning only a king can be added
        if current_card == None:
            return add_card.value == 13
        # The tableau contains a card of opposite value that is one less than the card to add
        return add_card.getColour() != current_card.getColour() and add_card.getValue() == current_card.getValue() - 1

    def addCards(self, cards):
        """ Appends the cards to the tableau if it's a valid move """
        if self.validMove(cards[0]):
            self.stack += cards
            return True
        return False
    def render(self, pygame, screen, font, position):
        """ Renders the cards of the tableau decending from the top card """
        cards = self.getStack()
        x, y = position
        card_width = 80
        card_height = 120
        card_gap = 50

        for i in range(len(cards)):
            cards[i].render(pygame, screen, font, (x, y + i * card_gap), (card_width, card_height))
            cards[i].setPositionAttributes((x, y + i * card_gap), (card_width, card_height))
        self.setPosition(position)
        self.setSideLengths((card_width, card_height + card_gap * len(cards)))
    
class Stock(Piles):
    """ Rotating deck of cards to be pulled into the Foundations or Tableau"""
    def rotate(self):
        """ Takes the current top card an inserts it into the bottom of the stock """
        self.stack.insert(0, self.stack.pop())
    def render(self, pygame, screen, font, position):
        """ Renders the cards of the tableau decending from the top card """
        x, y = position
        cards = self.getStack()
        card_width = 80
        card_height = 120
        cards[-1].render(pygame, screen, font, (x, y), (card_width, card_height))
        cards[-2].render(pygame, screen, font, (x + 100, y), (card_width, card_height))

        