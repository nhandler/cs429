import pygame, math, sys
from pygame.locals import *

BLACK = (0,0,0)

RES_FOLDER = "./"

class Game:
    fps = 30
    clock = None
    
    def __init__(self, size):
        self.size = size
        self.clock = pygame.time.Clock()
        

    def launch(self, game_state):
        
        game_state.screen = pygame.display.set_mode(self.size)
        while(1):
            print self.clock.tick(self.fps)
            game_state.events = pygame.event.get()
            for scene in game_state.updatable:
                if scene.should_update(game_state):
                    scene.update(game_state)
                    

            game_state.screen.fill(BLACK)
            for scene in game_state.renderable:
                if scene.should_render(game_state):
                    scene.render(game_state)
                 
            pygame.display.flip()
