import pygame
import json
import sys
import unittest
sys.path.insert(0,'../src')
from item import Item, MagicShoes
from locals import Direction, NEW_GAME_DIR
from player import PlayerSprite

class TestPlayer(unittest.TestCase):

    player = None
    load_player = None
    item = None
    screen = pygame.display.set_mode((600, 600))
    clock = pygame.time.Clock()
    BLACK = (0,0,0)
    background = pygame.Surface(screen.get_size())
    background = background.convert()
    background.fill(BLACK)

    def setUp(self):
        pygame.mixer.init()
        self.player = PlayerSprite((5, 5), (60, 60), Direction.up)
        self.item = MagicShoes

    def test_AddItemToInventory(self):
        inventory = self.player.inventory
        current_amount = inventory[self.item]
        self.player.addItemToInventory(self.item)
        self.assertEqual(inventory[self.item], current_amount + 1)

    def test_AddItemToInventoryNone(self):
        item = None
        inventory = self.player.inventory.copy()
        self.player.addItemToInventory(item)
        self.assertEqual(inventory, self.player.inventory)

    def test_finalInventory(self):
        pass
    
    def test_final_condition(self):
        pass

    def test_increment(self):
        incr = self.player.count
        self.player.increment_count()
        self.assertEquals(incr+1, self.player.count)

    def test_upgrade_weapon_t1(self):
        self.player.count = 5
        self.player.check_count()
        self.assertEquals(self.player.weapon_tier, 1)
        self.assertEquals(self.player.bullets, 2)

        self.player.count = 10
        self.player.check_count()
        self.assertEquals(self.player.weapon_tier, 2)
        self.assertEquals(self.player.laser, 2)

        self.player.count = 15
        self.player.check_count()
        self.assertEquals(self.player.weapon_tier, 3)
        self.assertEquals(self.player.laser, 3)
        self.assertEquals(self.player.bullets, 3)


    def test_load(self):
        data = json.loads(open('{0}player.json'.format(NEW_GAME_DIR)).read())

        self.load_player = PlayerSprite(json=data)
        self.assertEquals(self.player.health, self.load_player.health)
        self.assertEquals(self.player.lives, self.load_player.lives)
        self.assertEquals(self.player.inventory, self.load_player.inventory)
        self.assertEquals(self.player.final_inventory, self.load_player.final_inventory)
        self.assertEquals(self.player.count, self.load_player.count)
        self.assertEquals(self.player.bullets, self.load_player.bullets)
        self.assertEquals(self.player.weapon_tier, self.load_player.weapon_tier)
        self.assertEquals(self.player.laser, self.load_player.laser)
        self.assertEquals(self.player.action_wait_val, self.load_player.action_wait_val)
        self.assertEquals(self.player.iters_until_action, self.load_player.iters_until_action)
        self.assertEquals(self.player.direction, self.load_player.direction)
        self.assertEquals(self.player.coords, self.load_player.coords)
        self.assertEquals(self.player.width, self.load_player.width)
        self.assertEquals(self.player.height, self.load_player.height)
        #self.assertEquals(self.player, self.load_player)

    def test_save(self):
        player_json = self.player.to_json()
        loaded_json = json.loads(open('{0}player.json'.format(NEW_GAME_DIR)).read())
        self.assertEquals(player_json, loaded_json)


if __name__ == '__main__':
    unittest.main()

