import pygame 
from pygame.locals import *
from locals import SELECT, MENU_OPEN, MENU_CLOSE
from screen import Screen
from interactiveScreen import InteractiveScreen
from state import State


class InventoryScreen(InteractiveScreen):

	def __init__(self):
		super(InventoryScreen, self).__init__()
		self.lines = []
		for (item, amount) in State.inventory.iteritems():
			line = '{0} x {1}'.format(item.name, amount)
			self.lines.append(line)
	
	def render(self):
		black = (0, 0, 0)
		textColor = (255, 255, 0)
		monospace_font = pygame.font.SysFont('monospace', 15)
		State.screen.fill((0, 0, 0))
		title = monospace_font.render('Inventory:', 1, textColor)
		State.screen.blit(title, (100, 100))
		
		super(InventoryScreen, self).displayInteractiveLines(110, 10, 15)
		
	def update(self, events):
		for event in events:
			if not hasattr(event, 'key'): 
				continue
			if event.type == KEYDOWN:
				if event.key == K_i:
					self.sounds['close_menu'].play()
					State.pop_screen()
				elif event.key == K_RETURN:
					self.sounds['select'].play()
					i = 0
					for (item, amount) in State.inventory.iteritems():
						if i == self.currLine:
							if State.inventory[item] > 0:
								State.inventory[item] -= 1
								item.use()
								State.pop_screen()
						i += 1
				else:
					super(InventoryScreen, self).interact(event)

