import pygame 
from screen import Screen
from state import State

class VictoryScreen(Screen):

    def __init__(self, w, h):
        pygame.font.init()
        self.w = w
        self.h = h
        self.font = pygame.font.SysFont("monospace", 60)

    def render(self):
        temp = pygame.Surface(State.screen.get_size(), flags=pygame.SRCALPHA)
        temp.fill((0,0,0,1))
        label = self.font.render("You Win", 1, (255,255,255,1))
        (width, height) = self.font.size("You Win")
        temp.blit(label, (self.w/2 - width/2, self.h/2 - height/2))
        State.screen.blit(temp, (0,0))