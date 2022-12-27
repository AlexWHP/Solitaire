class Piles:
    def __init__(self) -> None:
        self.stack = []
    def resetStack(self):
        self.stack = []
    def getStack(self):
        return self.stack
    def setStack(self, cards):
        self.stack = cards
    def getTopCard(self):
        """ Returns the top card of the pile """
        if len(self.stack) > 0:
            return self.stack[-1]
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

class Foundation(Piles):
    """ Initially empty but aimed to be filled with a single ordered suit """
    def validMove(self, card):
        """ Valid if an ace is moved onto an empty foundation or is the same suit and one value higher than the current top card """
        if len(self.stack) > 0:
            return card.value == 1
        return card.suit != self.stack[-1].suit and self.stack[-1].value == card.value + 1
    def addCards(self, cards):
        """ Only singular cards can be added onto the foundation piles """
        if len(cards) == 1 and self.validMove(cards[0]):
            self.stack += cards
            return True
        return False

class Tableau(Piles):
    """ Workspace to help transfer cards to the Tableau """
    def validMove(self, add_card):
        """ Valid if the selected card can be placed on top of this card (Others can be assumed valid) """
        current_card = self.getTopCard()
        # The tableau is empty meaning only a king can be added
        if current_card == None:
            return add_card.value == 13
        # The tableau contains a card of opposite value that is one less than the card to add
        return add_card.colour != current_card.colour and add_card.value == current_card.value - 1

    def addCards(self, cards):
        """ Appends the cards to the tableau if it's a valid move """
        if self.validMove(cards[0]):
            self.stack += cards
            return True
        return False
    
class Stock(Piles):
    """ Rotating deck of cards to be pulled into the Foundations or Tableau"""
    def rotate(self):
        """ Takes the current top card an inserts it into the bottom of the stock """
        self.stack.insert(0, self.stack.pop())

        