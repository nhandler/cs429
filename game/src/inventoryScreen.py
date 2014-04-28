import pygame 
from pygame.locals import *
from locals import SELECT, MENU_OPEN, MENU_CLOSE
from screen import Screen
from interactiveScreen import InteractiveScreen
from state import State


class InventoryScreen(InteractiveScreen):

	def __init__(self, player):
		super(InventoryScreen, self).__init__()
		self.lines = []
		self.player = player
		for (item, amount) in self.player.inventory.iteritems():
			line = '{0} x {1}'.format(item.name, amount)
			self.lines.append(line)
			
	
	def render(self):
		black = (0, 0, 0)
		monospace_font = pygame.font.SysFont('monospace', 15)
		State.screen.fill((0, 0, 0))
		title = monospace_font.render('Inventory:', 1, InteractiveScreen.textColor)
		final_title = monospace_font.render('Tokens:', 1, InteractiveScreen.textColor)
		State.screen.blit(title, (180, 100))
		State.screen.blit(final_title, (10, 100))
		
		super(InventoryScreen, self).displayInteractiveLines(110, 10, 15)

		y = 110
        	for item in self.player.final_inventory:
            		line = monospace_font.render('{0}'.format(item.name), 1, (255, 255, 0))
            		State.screen.blit(line, (10, y))
            		y += 10
		
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
                    			for (item, amount) in self.player.inventory.iteritems():
                        			if i == self.currLine:
                           				if self.player.inventory[item] > 0:
                                				self.player.inventory[item] -= 1
                                				item.use(self.player)
                                				State.pop_screen()
                        			i += 1

				else:
					super(InventoryScreen, self).interact(event)

		    
