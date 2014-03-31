import pygame 
import math
import sys
from pygame.locals import *
from state import State
from screen import Screen


class InventoryScreen(Screen):
	
	def render(self):
		monospace_font = pygame.font.SysFont('monospace', 15)
        	State.screen.fill((0, 0, 0))
        	title = monospace_font.render('Inventory:', 1, (255, 255, 0))
		State.screen.blit(title, (100, 100))
		y = 110
		for item, amount in State.inventory:
			line = monospace_font.render('{0} x {1}'.format(item, amount), 1, (255, 255, 0))
			State.screen.blit(line, (100, y))
			y += 10
		
	def update(self, events):
		for event in events:
            		if not hasattr(event, 'key'): 
                		continue
            		if event.type == KEYDOWN:
                		if event.key == K_i:
                    			State.pop_screen()