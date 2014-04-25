import json
from time import sleep 
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
            self.weapon_tier = 0
        self.fire_sound = pymix.Sound(LASER)
        self.laser = 1

    def to_json(self):
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
        json['lives'] = self.lives

        return json

    def from_json(self, json):
        CreatureSprite.from_json(self, json)
        self.health = json['health']
        self.count = json['count']
        self.weapon_tier = json['wep_tier']
        self.lives = json['lives']
        items = get_items()
        for name, num in json['inventory'].items():
            for i in range(0, num):
                self.addItemToInventory(items[name])
        for name in json['final inventory']:
            self.addItemToInventory(items[name])

    def save(self, save_dir):
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
        if self.weapon_tier != tier:
            self.weapon_tier = tier

    def check_count(self):
        if self.count == 5:
            self.upgrade(1)
        elif self.count == 10:
            self.upgrade(2)
        elif self.count == 15:
            self.upgrade(3)

    def takeItem(self, source):
        self.addItemToInventory(source.item)
        source.item = None

    def fire(self, group):

        if self.weapon_tier == 0:
            bullet = BulletSprite(BULLET_IMAGE, self.coords, (self.width, self.height), self.direction)
            group.add(bullet)
        elif self.weapon_tier == 1:
            bullet1 = BulletSprite(BULLET_IMAGE, self.coords, (self.width + 5, self.height), self.direction)
            bullet2 = BulletSprite(BULLET_IMAGE, self.coords, (self.width, self.height), self.direction)
            group.add(bullet1)
            group.add(bullet2)
        elif self.weapon_tier == 2:
            self.laser += 1
        elif self.weapon_tier == 3:
            bullet1 = BulletSprite(BULLET_IMAGE, self.coords, (self.width + 5, self.height), self.direction)
            bullet2 = BulletSprite(BULLET_IMAGE, self.coords, (self.width, self.height), self.direction)
            bullet3 = BulletSprite(BULLET_IMAGE, self.coords, (self.width, self.height + 5), self.direction)
            group.add(bullet1)
            group.add(bullet2)
            group.add(bullet3)


    def increment_count(self):
        self.count += 1
        print self.count

    def check_final_condition(self):
        if(set([x for x in self.final_inventory]) == set(ItemType.final_items)):
            print "All final items collected!"
            State.boss_ready = True
            pymix.Sound(BOSS_READY).play(loops=2)
