import pygame 
import math
import sys
from pygame.locals import *
from player import PlayerSprite
from locals import Direction
from enemy import EnemySprite
from crate import ObjectSprite
from bullet import BulletSprite
from tileMap import *
from state import State
from item import Item, MagicShoes
from pauseScreen import *
from gameOverScreen import *
import random

def takeHit():
    if State.health > 0:
        State.health -= 1

class GameScreen(Screen):
    def __init__(self):
        self.tileMap = TileMap("../../maps/main_map.json")
        self.magicShoes = MagicShoes()
        self.crates = [
            ObjectSprite((1, 1), None),
            ObjectSprite((5, 7), None),
            ObjectSprite((2, 3), None),
            ObjectSprite((9, 5), None),
            ObjectSprite((9, 2), None),
            ObjectSprite((3, 6), self.magicShoes),
            ObjectSprite((7, 4), None),
            ObjectSprite((8, 8), None),
        ]
        
        self.crate_group = pygame.sprite.RenderPlain(*self.crates)
        #TODO get last argument of player constructor dynamically
        self.player = PlayerSprite('Hero.png', (5, 5), (60, 60))
        self.shooters = [
            #TODO get last argument of enemy constructor dynamically
            EnemySprite("enemy_red.png", (0, 0), (60, 60)),
            EnemySprite("enemy_red.png", (10, 10), (60, 60))
        ]
        self.enemies = [
            #TODO get last argument of enemy constructor dynamically
            EnemySprite("enemy_yellow.png", (0, 10), (60, 60)),
            EnemySprite("enemy_yellow.png", (10, 0), (60, 60))
        ]


        self.keyboard_input = {
            K_a: (KEYUP, KEYUP),
            K_d: (KEYUP, KEYUP),
            K_l: (KEYUP, KEYUP),
            K_s: (KEYUP, KEYUP),
            K_w: (KEYUP, KEYUP)
        }
        self.can_fire = True
        self.hits = 0

        self.player_group = pygame.sprite.RenderPlain(self.player)
        enemies = self.enemies + self.shooters
        self.enemy_group = pygame.sprite.RenderPlain(*enemies)
        self.bullet_group = pygame.sprite.Group()
        self.enemy_bullet_group = pygame.sprite.Group()
        self.player_group.update()
        self.enemy_group.update()
        
    def render(self):
        self.tileMap.draw(State.screen)
        self.crate_group.draw(State.screen)
        self.bullet_group.draw(State.screen)
        self.enemy_bullet_group.draw(State.screen)
        self.player_group.draw(State.screen)
        self.enemy_group.draw(State.screen)


    def update(self, events):
        
        self.handle_keyboard(events)
        self.player.handle_input(self.keyboard_input)

        for enemy in self.enemy_group:
            enemy.act()

        i = random.randint(1, 10)
        n = random.randint(1, 10)
        if i == n and self.shooters:
            self.enemy_fire(random.choice(self.shooters))

        self.check_collisions()
        if self.hits == 10:
            takeHit()
            self.hits = 0

        if(self.tileMap.update(self.player, self.enemy_group)):
            self.bullet_group.update()
            self.enemy_bullet_group.update()
            self.player_group.update()
            self.enemy_group.update()

        if State.health <= 0:
            State.push_screen(GameOverScreen(State.width*State.BLOCK_SIZE, State.height*State.BLOCK_SIZE))

    def handle_keyboard(self, events):
        
        self.keyboard_input = { 
            key: (new_val, new_val) 
            for key, (old_val, new_val) 
            in self.keyboard_input.items() 
        }

        for event in events:
            if not hasattr(event, 'key'): 
                continue
            if event.type == KEYDOWN:
                if event.key == K_p:
                    State.push_screen(PauseScreen())
                if event.key == K_i:
                    self.player.displayInventory()
                if event.key == K_l:
                    self.fire()
                    self.can_fire = False
                if event.key == K_h:
                    takeHit()
            elif event.type == KEYUP:
                if event.key == K_l: 
                    self.can_fire = True
                
            if event.key in self.keyboard_input:
                (old_val, new_val) = self.keyboard_input[event.key]
                self.keyboard_input[event.key] = (new_val, event.type)


    def check_collisions(self):
        player_crate_collisions = pygame.sprite.spritecollide(self.player, self.crate_group, False, self.did_player_crate_collide)
        player_enemy_collisions = pygame.sprite.spritecollide(self.player, self.enemy_group, False)
        if player_enemy_collisions:
            self.hits += 1

        for bullet in self.bullet_group:
            collisions = pygame.sprite.spritecollide(bullet, self.crate_group, False, self.did_crate_collide)
            for crate in collisions:
                self.bullet_group.remove(bullet)
            collisions = pygame.sprite.spritecollide(bullet, self.enemy_group, False, self.did_crate_collide)
            for enemy in collisions:
                self.bullet_group.remove(bullet)
                if enemy.health <= 0:
                    self.enemy_group.remove(enemy)
                    if enemy in self.shooters:
                        self.shooters.remove(enemy)
            (x, y) = bullet.coords
            if y < 0 or y > TileMap.height - 1: self.bullet_group.remove(bullet)
            if x < 0 or x > TileMap.width - 1: self.bullet_group.remove(bullet)

        for bullet in self.enemy_bullet_group:
            collisions = pygame.sprite.spritecollide(bullet, self.player_group, False)
            if collisions:
                self.enemy_bullet_group.remove(bullet)
                takeHit()
            (x, y) = bullet.coords
            if y < 0 or y > TileMap.height - 1: self.enemy_bullet_group.remove(bullet)
            if x < 0 or x > TileMap.width - 1: self.enemy_bullet_group.remove(bullet)
            
    def fire(self):
        if self.can_fire:
            bullet = BulletSprite('bullet.png', self.player.coords, self.player.direction)
            self.bullet_group.add(bullet)

    def enemy_fire(self, sprite):
        bullet = BulletSprite('enemy_bullet.png', sprite.coords, sprite.direction)
        self.enemy_bullet_group.add(bullet)


    def did_player_crate_collide(self, player_sprite, crate_sprite):
        if player_sprite.coords == crate_sprite.coords:
            crate_sprite.takeHit()
            self.player.takeItem(crate_sprite)
            return True
        else:
            return False

    def did_crate_collide(self, sprite_one, crate_sprite):
        if sprite_one.coords == crate_sprite.coords:
            crate_sprite.takeHit()
            return True
        else: 
            return False
