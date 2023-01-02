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
    def render(self, screen) -> None:
        """ Renders the card, icons, and numbers on the screen """
        pygame.draw.polygon(screen, (200, 200, 200), self.getVertices())

    def getPosition(self):
        return self.position
    def getSideLengths(self):
        return self.width, self.height
    def getVertices(self):
        return self.vertices

class SolitaireRender(Solitaire):
    def __init__(self):
        self.terminated = False
    def render(self):
        pygame.init()
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
            # Draw a solid blue circle in the center
            pygame.draw.circle(screen, (0, 0, 255), (250, 250), 75)
            c = CardRender((500, 500), self.deck.getCard(1))
            c.render(screen)
            # Flip the display
            pygame.display.flip()
        # Ending the game
        pygame.quit()

def main():
    """ Initialising values for Solitaire """
    s = SolitaireRender()
    s.createGame()
    s.render()
    print(s)
main()