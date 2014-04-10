import pygame 
import sys
from gameScreen import GameScreen
from pygame.locals import *
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
    State.screens = [GameScreen()]
    pygame.mixer.music.load('../res/sounds/opening.ogg')
    #pygame.mixer.music.set_volume(0.5)
    pygame.mixer.music.play(-1)

    while True:
        events = pygame.event.get()
        for event in events:
            if not hasattr(event, 'key'):
                continue
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    sys.exit(0)

        current_screen = State.screens[0]
        current_screen.update(events)
        current_screen.render()
        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
