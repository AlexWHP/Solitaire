from Solitaire import *
from CardDeck import *
from Piles import *

import pygame

class CardRender:
    def __init__(self, position, card) -> None:
        self.position = position
        self.card = card
        self.width = 80
        self.height = 140
        self.vertices = self.computeVertices()

    def computeVertices(self) -> list[tuple[float, float]]:
        """ Returns a list of vertices of the card as x, y tuples"""
        x, y = self.getPosition()
        width, height = self.getSideLengths()
        return [
            (x, y),
            (x, y + height),
            (x + width, y + height),
            (x + width, y)
        ]
    def render(self, screen, font) -> None:
        """ Renders the card, icons, and numbers on the screen """
        card = self.getCard()
        x, y = self.getPosition()

        # Rendering of the card
        pygame.draw.polygon(screen, (200, 200, 200), self.getVertices())
        pygame.draw.lines(screen, (0, 0, 0), True, self.getVertices())
        # Rendering of the suit
        text_surface = font.render(str(card), False, (0, 0, 0))
        screen.blit(text_surface, (x, y))
        # Rendering of the number

    def getPosition(self):
        return self.position
    def getCard(self):
        return self.card
    def getSideLengths(self):
        return self.width, self.height
    def getVertices(self):
        return self.vertices

class PileRender:
    def __init__(self, position, pile) -> None:
        self.position = position
        self.pile = pile

    def render(self, screen, font):
        raise NotImplementedError

    def getPosition(self):
        return self.position
    def getPile(self):
        return self.pile

class FoundationRender(PileRender):
    def __init__(self, position, foundation) -> None:
        super().__init__(position, foundation)

    def render(self, screen, font):
        """ Renders the foundation cards horizontally """
        foundation = self.getPile()
        cards = foundation.getStack()
        for i in range(len(cards)):
            x, y = self.getPosition()
            c = CardRender((x + 100 * i, y), cards[i])
            c.render(screen, font)

class TableauRender(PileRender):
    def __init__(self, position, tableau) -> None:
        super().__init__(position, tableau)

    def render(self, screen, font):
        """ Renders the cards of the tableau decending from the top card """
        tableau = self.getPile()
        cards = tableau.getStack()
        for i in range(len(cards)):
            x, y = self.getPosition()
            c = CardRender((x, y + 50 * i), cards[i])
            c.render(screen, font)


class StockRender(PileRender):
    def __init__(self, position, stock) -> None:
        super().__init__(position, stock)

    def render(self, screen, font):
        stock = self.getPile()
        cards = stock.getStack()
        x, y = self.getPosition()
        c = CardRender((x, y), cards[-1])
        c.render(screen, font)
        c = CardRender((x + 100, y), cards[-2])
        c.render(screen, font)

class SolitaireRender(Solitaire):
    def __init__(self):
        self.terminated = False
    def render(self):
        pygame.init()
        font = pygame.font.SysFont("Comic Sans MS", 30)
        screen = pygame.display.set_mode((1400, 800))
        pygame.display.set_caption('Solitaire')
        # Sets Font
        self.font = pygame.font.Font('freesansbold.ttf', 24)

        self.clock = pygame.time.Clock()
        while not self.terminated:
            # Checks for events from the window
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.terminated = True
            # Fill the background with white
            screen.fill((255, 255, 255))

            # Rendering the foundations
            fons = self.getFoundations()
            for i in range(len(fons)):
                f = FoundationRender((0 + i * 100, 0), fons[i])
                f.render(screen, font)
            # Rendering the tableaus
            tabs = self.getTableaus()
            for i in range(len(tabs)):
                t = TableauRender((400 + i * 100, 200), tabs[i])
                t.render(screen, font)
            # Rendering the stocks
            s = StockRender((600, 0), self.getStock())
            s.render(screen, font)

            # Flip the display
            pygame.display.flip()
        # Ending the game
        pygame.quit()

def main():
    """ Initialising values for Solitaire """
    s = SolitaireRender()
    s.createGame()
    s.render()
main()