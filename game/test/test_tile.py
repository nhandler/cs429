"""import pygame, sys
from pygame.locals import *
from cs429.game.src.tile import Tile

FPS = 30
fpsClock = pygame.time.Clock()

# Manual test to load images from tileset/example.tmx
def main():
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((1000, 800))
    new_tile = Tile('./cs429/game/test/tileset/example.tmx')

    while True:
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit

        new_tile.draw_background(DISPLAYSURF)
        new_tile.draw_foreground(DISPLAYSURF)
        new_tile.draw_top(DISPLAYSURF)
        pygame.display.update()

        fpsClock.tick(FPS)

if __name__ == '__main__':
    main()"""

