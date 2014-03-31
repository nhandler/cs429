import pygame 
import math
import sys
from pygame.locals import *
from state import State
from screen import Screen


class InventoryScreen(Screen):

	def __init__(self):
		self.currLine = 0
	
	def render(self):
		monospace_font = pygame.font.SysFont('monospace', 15)
		State.screen.fill((0, 0, 0))
		title = monospace_font.render('Inventory:', 1, (255, 255, 0))
		State.screen.blit(title, (100, 100))
		i = 0
		y = 110
		for (item, amount) in State.inventory.iteritems():
			if i == self.currLine:
				line = monospace_font.render('> {0} x {1}'.format(item.name, amount), 1, (255, 255, 0))
			else:
				line = monospace_font.render('  {0} x {1}'.format(item.name, amount), 1, (255, 255, 0))
			State.screen.blit(line, (100, y))
			y += 10
			i += 1
		
	def update(self, events):
		for event in events:
			if not hasattr(event, 'key'): 
				continue
			if event.type == KEYDOWN:
				if event.key == K_i:
					State.pop_screen()
				elif event.key == K_w:
					self.currLine -= 1
					if self.currLine < 0:
						self.currLine = 0
				elif event.key == K_s:
					self.currLine += 1
					if self.currLine >= len(State.inventory):
						self.currLine = len(State.inventory) - 1
				elif event.key == K_RETURN:
					i = 0
					for (item, amount) in State.inventory.iteritems():
						if i == self.currLine:
							State.inventory[item] -= 1
							item.use()
							State.pop_screen()
						i += 1

