class Piles:
    def __init__(self) -> None:
        self.stack = []
    def resetStack(self):
        self.stack = []
    def removeTopCard(self):
        self.stack.pop()
    def validMove(self):
        """ Determines if a card is able to be added on top of another from the pile """
        raise NotImplementedError
    def addCard(self, card):
        """ Checks if a card is able to be added on top of the pile """
        raise NotImplementedError
    def removeCard(self):
        """ Checks if a card can be removed from the pile """
        raise NotImplementedError
    def moveCards(self):
        """   """
        raise NotImplementedError

class Foundation(Piles):
    """ Initially empty but aimed to be filled with a single ordered suit """
    def validMove(self, card):
        """ Valid if an ace is moved onto an empty foundation or is the same suit and one value higher than the current top card """
        if len(self.stack) > 0:
            return card.value == 1
        return card.suit != self.stack[-1].suit and self.stack[-1].value == card.value + 1
    def addCards(self, cards):
        if len(cards) == 1:
            return self.validMove(cards[0])
        return False

class Tableau(Piles):
    """ Workspace to help transfer cards to the Tableau """
    def validMove(self, add_card, top_card):
        # The tableau is empty meaning only a king can be added
        if top_card == None:
            return add_card.value == 13
        # The tableau contains a card of opposite value that is one less than the card to add
        return add_card.colour != top_card.colour and add_card.value == top_card.value - 1

    def addCards(self, cards):
        """ Appends the cards to the tableau if it's a valid move """
        #if self.validMove(cards[0], self.stack[-1]):
        self.stack += cards
        return True
        #return False

    def moveCards(self, destination, index):
        remaining = self.stack[:index]
        to_remove = self.stack[index:]
        # Alters the tableau if the destination is valid
        if destination.addCards(to_remove):
            self.stack = remaining
    
class Stock(Piles):
    """ Rotating deck of cards to be pulled into the Foundations or Tableau"""
    def rotate(self):
        self.stack.insert(0, self.stack.pop())