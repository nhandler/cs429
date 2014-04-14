import pygame 
from pygame.locals import *
from locals import SELECT, MENU_OPEN, MENU_CLOSE
from screen import Screen
from state import State


class InventoryScreen(Screen):

	def __init__(self):
		self.currLine = 0
		self.sound = pygame.mixer.Sound(MENU_OPEN)
		self.sound.play()
		self.sounds = {
            'select': pygame.mixer.Sound(SELECT),
            'close_menu': pygame.mixer.Sound(MENU_CLOSE),
            'menu': pygame.mixer.Sound(MENU_OPEN),
        }
	
	def render(self):
		monospace_font = pygame.font.SysFont('monospace', 15)
		State.screen.fill((0, 0, 0))
		title = monospace_font.render('Inventory:', 1, (255, 255, 0))
		State.screen.blit(title, (150, 100))
		i = 0
		y = 110
		for (item, amount) in State.inventory.iteritems():
			if i == self.currLine:
				line = monospace_font.render('> {0} x {1}'.format(item.name, amount), 1, (255, 255, 0))
			else:
				line = monospace_font.render('  {0} x {1}'.format(item.name, amount), 1, (255, 255, 0))
			State.screen.blit(line, (250, y))
			y += 10
			i += 1

                y = 110
                for item in State.player.final_inventory:
                        line = monospace_font.render('{0}'.format(item.name), 1, (255, 255, 0))
                        State.screen.blit(line, (50, y))
                        y += 10
                	
	def update(self, events):
		for event in events:
			if not hasattr(event, 'key'): 
				continue
			if event.type == KEYDOWN:
				if event.key == K_i:
					self.sounds['close_menu'].play()
					State.pop_screen()
				elif event.key == K_w:
					self.sounds['select'].play()
					if self.currLine > 0:
						self.currLine -= 1
				elif event.key == K_s:
					self.sounds['select'].play()
					if self.currLine+1 < len(State.inventory):
						self.currLine += 1
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

