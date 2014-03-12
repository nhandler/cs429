import pygame 
import math
import sys
from pygame.locals import *
from state import *
from screen import *


class PauseScreen(Screen):

    def render(self):
        monospace_font = pygame.font.SysFont('monospace', 15)
        State.screen.fill((0, 0, 0))
        title = monospace_font.render('Game Paused', 1, (255, 255, 0))
        health = monospace_font.render('Health: {0}'.format(State.health), 1, (255, 255, 0))
        State.screen.blit(title, (100, 100))
        State.screen.blit(health, (100, 110))

    def update(self, events):
        for event in events:
            if not hasattr(event, 'key'): 
                continue
            if event.type == KEYDOWN:
                if event.key == K_p:
                    State.pop_screen()
