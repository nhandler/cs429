from creature import CreatureSprite
from locals import Direction
from pygame.locals import *
from item import Item, ItemType, MagicShoes

class PlayerSprite (CreatureSprite):
    def __init__(self, image, position):
        CreatureSprite.__init__(self, image, position)
        self.inventory = {}

    def handle_input(self, keyboard_input):
        def handle_movement_keys(key, direction):
            if self.can_take_action() and key in keyboard_input:
                (new_val, old_val) = keyboard_input[key]
                if new_val == KEYDOWN:
                    self.direction = direction
                    self.action_taken()
                if old_val == new_val == KEYDOWN:
                    self.move(direction)
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
        if item.name not in self.inventory:
            self.inventory[item.name] = 0
        self.inventory[item.name] += 1

    def takeItem(self, source):
        self.addItemToInventory(source.item)
        source.item = None

    def displayInventory(self):
        print 'Inventory:'
        for itemtype in self.inventory:
            print itemtype, " x ", self.inventory[itemtype]
