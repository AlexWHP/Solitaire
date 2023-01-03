from CardDeck import *
from Piles import *

class Solitaire:
    def __init__(self) -> None:
        """ Generates the deck and the piles of the game """
        self.deck = Deck()
        self.foundations = dict.fromkeys({temp: []for temp in range(4)}, Foundation())
        for i in self.foundations:
            self.foundations[i] = Foundation()
        self.tableaus = dict.fromkeys({temp: []for temp in range(7)}, None)
        for i in self.tableaus:
            self.tableaus[i] = Tableau()
        self.stock = dict.fromkeys({temp: []for temp in range(2)}, None)
        for i in self.stock:
            self.stock[i] = Stock()
        self.resetGame()

    def resetGame(self):
        """ Resets the game of Solitaire """
        deck = self.getDeck()
        deck.hideCards()
        deck.shuffle()
        deck_index = 0
        # Populate the tableaus
        for i in range(len(self.getTableaus())):
            cards = []
            for j in range(i + 1):
                card = deck.getCard(deck_index)
                cards.append(card)
                if j == i:
                    card.reveal()
                deck_index += 1
            self.getTableau(i).setStack(cards)
        # Populate the stock and reveal the top card of it
        stock = self.getStock()
        stock[0].setStack(deck.getCards()[deck_index:-1])
        stock[1].setStack([deck.getCards()[-1]])
        deck.getCard(-1).reveal()

    def moveCards(self, cards, origin, destination):
        """ Attempts to move the cards from the origin onto the destination """
        if destination.addCards(cards):
            origin.removeCards(cards)

    def mouseClick(self, point):
        """ Handles the mouse click and the meaning it could have for the game """
        piles = self.getFoundations()
        for i in range(len(piles)):
            if piles[i].collideWithPoint(point):
                print(piles[i])
                return
        piles = self.getTableaus()
        for i in range(len(piles)):
            if piles[i].collideWithPoint(point):
                print(piles[i])
                cards = piles[i].collideWithCards(point)
                print(cards)
                print()
                if piles[i].removeCards(cards):
                    return cards
                return None
        piles = self.getStock()
        for i in range(len(piles)):
            if piles[i].collideWithPoint(point):
                print(piles[i])
                return
        return
    
    def getDeck(self) -> Deck():
        """  Returns the deck of cards associated with the game """
        return self.deck
    def getFoundations(self) -> Foundation:
        """ Returns the foundations of the game"""
        return self.foundations
    def getTableau(self, index) -> Tableau:
        """ Returns the tableau of a specific column """
        return self.tableaus[index]
    def getTableaus(self) -> dict():
        """ Returns all of the tableaus of the game """
        return self.tableaus
    def getStock(self) -> dict():
        return self.stock

    def render(self, pygame, screen, font):
        """ Renders the Solitaire game given its current state """
        fons = self.getFoundations()
        for i in range(len(fons)):
            fons[i].render(pygame, screen, font, (0 + 100 * i, 0))
        # Rendering the tableaus
        tabs = self.getTableaus()
        for i in range(len(tabs)):
            tabs[i].render(pygame, screen, font, (400 + i * 100, 200))
        # Rendering the stocks
        sto = self.getStock()
        for i in range(len(sto)):
            sto[i].render(pygame, screen, font, (600, 0))