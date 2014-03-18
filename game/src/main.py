import pygame 
import math
import sys
from pygame.locals import *
from player import PlayerSprite
from locals import Direction
from enemy import EnemySprite
from crate import ObjectSprite
from bullet import BulletSprite
from state import State
from item import Item, MagicShoes
from pauseScreen import PauseScreen
from gameScreen import GameScreen
from tileMap import TileMap

pygame.init()

screen = pygame.display.set_mode(
    (TileMap.width*TileMap.BLOCK_SIZE, TileMap.height*TileMap.BLOCK_SIZE)
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
