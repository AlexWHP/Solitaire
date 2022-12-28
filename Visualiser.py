from Solitaire import *
from CardDeck import *
from Piles import *

import pygame

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