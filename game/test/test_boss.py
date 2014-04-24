import pygame
import sys
import unittest
sys.path.insert(0,'../src')
from boss import BossSprite
from locals import Direction

class MockTile():
    def is_walkable(self, x, y):
        return True

class TestBoss(unittest.TestCase):
    
    boss = None
    screen = pygame.display.set_mode((600,600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    def setUp(self):
        pygame.mixer.init()
        self.boss = BossSprite((5,5), (60, 60))

    def test_BossJson(self):
        self.assertEqual(self.boss.to_json(), {'action_wait_val': 12, 'direction': 1, 'height': 60, 'width': 60, 'health': 50, 'y': 5, 'x': 5, 'iters_until_action': 0})
        self.boss.from_json({'action_wait_val': 15, 'direction': 2, 'height': 20, 'width': 20, 'health': 20, 'y': 10, 'x': 10, 'iters_until_action': 0})
        self.assertEqual(self.boss.health, 20)
    
    def test_BossMove(self):
        coords = self.boss.coords
        self.boss.act(MockTile())
        self.assertNotEqual(coords, self.boss.coords)

    def test_BossShouldShoot(self):
        (x, y) = self.boss.coords

        #probability that this won't catch an error: 1/10^20
        for i in range(0, 20):
            self.assertFalse(self.boss.shouldShoot(x, y))

        #probability that this won't catch an error: 2.66 E-5
        flag = False
        for i in range(0, 100):
            flag = flag or self.boss.shouldShoot(x + 1, y + 1)
        self.assertTrue(flag)

    def test_BossOOB(self):
        self.boss.direction = Direction.right
        self.boss.handleOutOfBounds(0, 0, 0, 0, 0, 0)
        self.assertEqual(self.boss.direction, Direction.left)

if __name__ == '__main__':
    unittest.main()
