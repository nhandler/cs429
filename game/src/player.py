import json
from creature import CreatureSprite
from bullet import BulletSprite
from item import Item, ItemType, MagicShoes, Potion, Crystal, FinalItem1, FinalItem2, get_items
from locals import Direction, BULLET_IMAGE, PLAYER_IMAGE, LASER, BOSS_READY
from pygame.locals import *
import pygame.mixer as pymix
from state import State

class PlayerSprite (CreatureSprite):
    std_health = 10
    std_lives = 3

    def __init__(self, position=(0, 0), size=(0, 0), direction=Direction.down, json=None):
        CreatureSprite.__init__(self, PLAYER_IMAGE, position, size, direction)
        if json:
            self.inventory = {}
            self.final_inventory = []
            self.from_json(json)
        else:
            self.lives = self.std_lives
            self.health = self.std_health
            self.inventory = {MagicShoes : 2, Item : 1, Potion : 2, Crystal : 3}
            self.final_inventory = []
            self.count = 0
            self.bullets = 1
            self.weapon_tier = 0
        self.fire_sound = pymix.Sound(LASER)
        self.laser = 1

    def to_json(self):
        '''
        Serialize the important members of this class as a json object
        '''

        json = CreatureSprite.to_json(self)
        json['health'] = self.health
        json['count'] = self.count
        json['wep_tier'] = self.weapon_tier
        json['inventory'] = {}
        for item, num in self.inventory.items():
            json['inventory'][item.name] = num
        json['final inventory'] = []
        for item in self.final_inventory:
            json['final inventory'].append(item.name)
        json["bullets"] = self.bullets
        json['lives'] = self.lives

        return json

    def from_json(self, json):
        '''
        Restore this object from the passed in json object

        @param json - the json object
        '''

        CreatureSprite.from_json(self, json)
        self.health = json['health']
        self.count = json['count']
        self.weapon_tier = json['wep_tier']
        self.lives = json['lives']
        self.bullets = json['bullets']
        items = get_items()
        for name, num in json['inventory'].items():
            for i in range(0, num):
                self.addItemToInventory(items[name])
        for name in json['final inventory']:
            self.addItemToInventory(items[name])

    def save(self, save_dir):
        '''
        saves the current state of the player

        @param save_dir - directory that the current game is saved to
        '''

        with open('{0}player.json'.format(save_dir), 'w') as f:
            f.write(json.dumps(self.to_json()))

    def handle_input(self, keyboard_input, tile, bullet_group):
        def handle_movement_keys(key, direction):
            if self.can_take_action() and key in keyboard_input:
                (old_val, new_val) = keyboard_input[key]
                if new_val == KEYDOWN:
                    if self.direction == direction:
                        self.move(direction, tile)
                    else:
                        self.direction = direction
                    self.action_taken()

        for key, direction in [
            (K_w, Direction.up), 
            (K_s, Direction.down),
            (K_a, Direction.left),
            (K_d, Direction.right)
        ]:
            handle_movement_keys(key, direction)
            self.iters_until_action -= 1

        if keyboard_input[K_l] == (KEYUP, KEYDOWN):
            self.fire_sound.play()
            self.fire(bullet_group)

        if keyboard_input[K_h] == (KEYUP, KEYDOWN):
            self.takeHit(1)

    def addItemToInventory(self, item):
        '''
            Adds an item to player's inventory

            @param item - item to be added
        '''

        if item is None:
            return
        if item in ItemType.final_items:
            self.final_inventory.append(item)
            self.check_final_condition()
        else:
            if item not in self.inventory:
                self.inventory[item] = 0
            self.inventory[item] += 1

    def upgrade(self, tier):
        '''
            Upgrades the player's weapon based

            @param tier - tier to be upgraded to
        '''
        if self.weapon_tier >= tier:
            return 
        elif tier == 1:
            self.bullets = 2
        elif tier == 2:
            self.laser += 1
        elif tier == 3:
            self.laser += 1
            self.bullets = 3

    def check_count(self):
        '''
            Checks to see if the player is ready to have their weapon
            upgraded
        '''

        if self.count == 5:
            self.upgrade(1)
            self.weapon_tier = 1
        elif self.count == 10:
            self.upgrade(2)
            self.weapon_tier = 2
        elif self.count == 15:
            self.upgrade(3)
            self.weapon_tier = 3

    def takeItem(self, source):
        '''
            Function to take an item from the source

            @param source - The thing that is holding the item
        '''
        self.addItemToInventory(source.item)
        source.item = None

    def fire(self, group):
        '''
        Fires the bullet(s)

        @param group - The group that the bullets will be added to
        '''

        for i in range(self.bullets):
            group.add(BulletSprite(BULLET_IMAGE, self.coords, (self.width + i, self.height), self.direction))

    def increment_count(self):
        '''
        increments the enemies killed counter
        '''

        self.count += 1

    def check_final_condition(self):
        '''
        Checks to see if the final condition to meet the boss has been met
        '''
        
        if(set([x for x in self.final_inventory]) == set(ItemType.final_items)):
            print "All final items collected!"
            State.boss_ready = True
            pymix.Sound(BOSS_READY).play(loops=2)
