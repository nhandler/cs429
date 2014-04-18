import pygame
import sys
import unittest
sys.path.insert(0, '../src')
from gameScreen import GameScreen
from locals import Direction, NEW_GAME_DIR
from player import PlayerSprite
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
		self.screen = GameScreen(NEW_GAME_DIR)
		
		State.screen = self.screen
		self.player = PlayerSprite((5, 5), (60, 60), Direction.down)
		self.creature_collide = PlayerSprite((5, 5), (60, 60), Direction.up)
		self.creature_miss = PlayerSprite((5, 4), (60, 60), Direction.up)

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
