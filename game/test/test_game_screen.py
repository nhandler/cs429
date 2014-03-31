import pygame
import math
import sys

from pygame.locals import *
sys.path.append('../src')
import unittest

from gameScreen import GameScreen
import gameScreen
from player import PlayerSprite
from locals import Direction
from creature import CreatureSprite
from state import State

class TestGameScreen(unittest.TestCase):

	screen = None
	player = None
	creature_collide = None
	creature_miss = None
	State.screen = None
	State.health = 0

	def setUp(self):
		pygame.init()
		screen = pygame.display.set_mode((800, 600))
		self.screen = GameScreen()
		
		State.health = 1
		State.screen = self.screen
		self.player = PlayerSprite('Hero.png', (5, 5), (60, 60), Direction.down)
		self.creature_collide = PlayerSprite('Hero.png', (5, 5), (60, 60), Direction.up)
		self.creature_miss = PlayerSprite('Hero.png', (5, 4), (60, 60), Direction.up)

	def test_take_hit(self):
		gameScreen.takeHit()
		self.assertEqual(State.health, 0)

	def test_player_collide(self):
		collide = self.screen.player_enemy_collide(self.player, self.creature_collide)
		self.assertEqual(True, collide)

	def test_player_miss(self):
		collide = self.screen.player_enemy_collide(self.player, self.creature_miss)
		self.assertEqual(False, collide)

	def test_opposite_direction_up(self):
		direction = Direction.up
		correctDir = Direction.down

		direction = self.screen.oppositeDirection(direction)
		self.assertEqual(direction, correctDir)

	def test_opposite_direction_down(self):
		direction = Direction.down
		correctDir = Direction.up

		direction = self.screen.oppositeDirection(direction)
		self.assertEqual(direction, correctDir)

	def test_opposite_direction_left(self):
		direction = Direction.left
		correctDir = Direction.right

		direction = self.screen.oppositeDirection(direction)
		self.assertEqual(direction, correctDir)

	def test_opposite_direction_right(self):
		direction = Direction.right
		correctDir = Direction.left

		direction = self.screen.oppositeDirection(direction)
		self.assertEqual(direction, correctDir)


if __name__ == '__main__':
    unittest.main()
