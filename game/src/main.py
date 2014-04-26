import pygame
import shutil
import sys
from gameMenuScreen import GameMenuScreen
from pygame.locals import *
from locals import GAME_MUSIC, CURRENT_GAME_DIR
from state import State
from tileMap import TileMap


pygame.mixer.pre_init(44100, -16, 2, 2048)
pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode(
    (TileMap.width*TileMap.BLOCK_SIZE[0], TileMap.height*TileMap.BLOCK_SIZE[1])
)
clock = pygame.time.Clock()
BLACK = (0,0,0)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BLACK)


State.screen = screen
screen.blit(background, (0, 0))
pygame.display.flip()


def main():
    State.screens = [GameMenuScreen()]
    pygame.mixer.music.load(GAME_MUSIC)
    #pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == KEYDOWN and event.key == K_ESCAPE:
                shutil.rmtree(CURRENT_GAME_DIR, ignore_errors=True)
                sys.exit(0)

        current_screen = State.screens[0]
        current_screen.update(events)
        current_screen.render()
        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
