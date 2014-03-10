

import pygame 
from pygame.locals import *

class GameOver(object):

    def __init__(self, w, h):
        pygame.font.init()
        self.w = w
        self.h = h
        self.font = pygame.font.SysFont("monospace", 60)

    def update(self):
        return

    def render(self, surface):
        temp = pygame.Surface(surface.get_size(), flags=pygame.SRCALPHA)
        temp.fill((0,0,0,1))
        label = self.font.render("Game Over", 1, (255,255,255,1))
        (width, height) = self.font.size("Game Over")
        temp.blit(label, (self.w/2 - width/2, self.h/2 - height/2))
        surface.blit(temp, (0,0))
        return
