import pygame 
from inventoryScreen import InventoryScreen
from pygame.locals import *
from screen import Screen
from state import State


class PauseScreen(Screen):
    def __init__(self, player):
        self.health = player.health

    def render(self):
        monospace_font = pygame.font.SysFont('monospace', 15)
        State.screen.fill((0, 0, 0))
        title = monospace_font.render('Game Paused', 1, (255, 255, 0))
        health = monospace_font.render('Health: {0}'.format(self.health), 1, (255, 255, 0))
        State.screen.blit(title, (100, 100))
        State.screen.blit(health, (100, 110))

    def update(self, events):
        for event in events:
            if not hasattr(event, 'key'): 
                continue
            if event.type == KEYDOWN:
                if event.key == K_p:
                    State.pop_screen()
		elif event.key == K_i:
		    State.push_screen(InventoryScreen())
