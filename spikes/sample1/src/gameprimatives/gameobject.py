import pygame, math, sys
from pygame.locals import *

class GameObject(object):
    image = None
    position = (0,0)
    rotation = 0    
        
    def update(self, game_state):
        return

    def render(self, game_state):
        rotated = pygame.transform.rotozoom(self.image, self.rotation, 1)
        rect = rotated.get_rect()
        rect.center = self.position
        game_state.screen.blit(rotated, rect)
        
    def should_update(self, game_state):
        return True

    def should_render(self, game_state):
        return True

    def cleanup(self, game_state):
        print "cleaning up" + str(self)
        return
