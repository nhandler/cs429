import pygame
from pygame.locals import *
from gameprimatives.gamescene import *

class MenuScene(GameScene):

    current_item = None
    items = None

    def __init__(self, items):
        if not pygame.font.get_init():
            pygame.font.init()
        self.current_item = 0
        self.items = items

    def update(self, game_state):
        for event in game_state.events:
            if not hasattr(event, 'key') or event.type != KEYDOWN: continue
            if event.key == K_UP: self.decrease()
            elif event.key == K_DOWN: self.increase()
            elif event.key == K_q: game_state.pop_scene()


    def render(self, game_state):
        bigfont = pygame.font.SysFont("monospace", 20)
        myfont = pygame.font.SysFont("monospace", 15)
        for item, index in zip(self.items, range(0, len(self.items))):
            if index == self.current_item:
                label = bigfont.render(item, 1, (255,255,255))
            else:
                label = myfont.render(item, 1, (255,255,255))
            game_state.screen.blit(label, (300, 100 + (20 * index)))

    def increase(self):
        self.current_item = (self.current_item + 1) % len(self.items)

    def decrease(self):
        if self.current_item == 0:
            self.current_item = len(self.items)-1
        else:
            self.current_item -= 1
