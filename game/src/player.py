from creature import CreatureSprite
from bullet import BulletSprite
from item import Item, MagicShoes
from locals import Direction
from pygame.locals import *

class PlayerSprite (CreatureSprite):
    def __init__(self, image, position, size, direction):
        CreatureSprite.__init__(self, image, position, size, direction)
        self.health = 10
	magicShoes = MagicShoes()
	other = Item()
        self.inventory = {magicShoes : 2, other : 1}

    def to_json(self):
        json = CreatureSprite.to_json(self)
        json['health'] = self.health
        # TODO add support for inventory
        return json

    def from_json(self, json):
        CreatureSprite.from_json(self, json)
        self.health = json['health']
        # TODO add support for inventory

    def handle_input(self, keyboard_input, tile):
        def handle_movement_keys(key, direction):
            if self.can_take_action() and key in keyboard_input:
                (old_val, new_val) = keyboard_input[key]
                if new_val == KEYDOWN:
                    if self.direction == direction:
                        self.move(direction, tile)
                    else:
                        self.direction = direction
                    self.action_taken()
                if old_val == new_val == KEYDOWN:
                    self.move(direction, tile)
                    self.action_taken()

        for key, direction in [
            (K_w, Direction.up), 
            (K_s, Direction.down),
            (K_a, Direction.left),
            (K_d, Direction.right)
        ]:
            handle_movement_keys(key, direction)
            self.iters_until_action -= 1

    def addItemToInventory(self, item):
        if item is None:
            return
        if item not in self.inventory:
            self.inventory[item] = 0
        self.inventory[item] += 1

    def takeItem(self, source):
        self.addItemToInventory(source.item)
        source.item = None

    def fire(self, group):
        bullet = BulletSprite('../res/bullet.png', self.coords, (self.width, self.height), self.direction)
        group.add(bullet)
