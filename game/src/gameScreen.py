import json
import pygame
from bullet import BulletSprite
from gameOverScreen import GameOverScreen
from victoryScreen import VictoryScreen
from inventoryScreen import InventoryScreen
from locals import Direction, LASER
from pauseScreen import PauseScreen
from player import PlayerSprite
from pygame.locals import *
from screen import Screen
from state import State
from tileMap import TileMap

class GameScreen(Screen):
    def __init__(self, save_dir):
        '''
        Initializes the main screen that gameplay takes place on

        @param save_dir - The directory to be saved to
        '''
        self.sound = pygame.mixer.Sound(LASER)
        self.tileMap = TileMap(save_dir)
        
        self.crate_group = pygame.sprite.RenderPlain(*self.tileMap.tile.crates)
        data = json.loads(open('{0}player.json'.format(save_dir)).read())
        self.player = PlayerSprite(json=data)
        self.button_group = pygame.sprite.RenderPlain(*self.tileMap.tile.buttons)
        self.gate_group = pygame.sprite.RenderPlain(*self.tileMap.tile.gates)

        self.keyboard_input = {
            K_a: (KEYUP, KEYUP),
            K_d: (KEYUP, KEYUP),
            K_l: (KEYUP, KEYUP),
            K_s: (KEYUP, KEYUP),
            K_w: (KEYUP, KEYUP),
            K_h: (KEYUP, KEYUP)
        }

        self.player_group = pygame.sprite.RenderClear(self.player)
        self.enemies = self.tileMap.tile.enemies
        self.boss = self.tileMap.tile.bosses
        self.shooters = self.tileMap.tile.shooters + self.boss
        enemies = self.enemies + self.shooters
        self.enemy_group = pygame.sprite.RenderPlain(*enemies)
        self.bullet_group = pygame.sprite.Group()
        self.enemy_bullet_group = pygame.sprite.Group()
        self.player_group.update()
        self.enemy_group.update()

    def render(self):
        '''
        Renders each of the groups to the main game screen

        That includes tile, crates, button, bullets, enemies and the player
        '''

        self.tileMap.draw(State.screen)
        self.crate_group.draw(State.screen)
        self.button_group.draw(State.screen)
        self.gate_group.draw(State.screen)
        self.bullet_group.draw(State.screen)
        self.enemy_bullet_group.draw(State.screen)
        self.player_group.draw(State.screen)
        self.enemy_group.draw(State.screen)

    def reset_sprite_groups(self):
        '''
        Resets each of the sprite groups back to their original parameters
        '''
        self.crate_group = pygame.sprite.RenderPlain(*self.tileMap.tile.crates)
        self.button_group = pygame.sprite.RenderPlain(*self.tileMap.tile.buttons)
        self.gate_group = pygame.sprite.RenderPlain(*self.tileMap.tile.gates)
        self.enemies = self.tileMap.tile.enemies
        self.boss = self.tileMap.tile.bosses
        self.shooters = self.tileMap.tile.shooters + self.boss
        enemies = self.enemies + self.shooters
        self.enemy_group = pygame.sprite.RenderPlain(*enemies)

    def update(self, events):
        '''
        Updates everything in the game

        This includes: 
            - checking to see if the final condition has been met
            - handling keybour events
            - Checking kill count
            - Having each enemy call their act functions
            - Checking collisions
            - Updating each tile
            - Checking the health of the player

        '''
        if State.boss_ready:
            self.gate_group.empty()
            self.tileMap.tile.gates = []

        self.handle_keyboard(events)
        self.player.handle_input(self.keyboard_input, self.tileMap.tile, self.bullet_group)
        self.player.check_count()
        
        for enemy in self.enemy_group:
            enemy.act(self.tileMap.tile)

        for shooter in self.shooters:
            (px, py) = self.player.coords
            if shooter.shouldShoot(px, py): 
                shooter.shoot(shooter, self.enemy_bullet_group)

        self.check_collisions()

        if(self.tileMap.update(self.player, self.enemy_group)):
            self.bullet_group.update()
            self.enemy_bullet_group.update()
            self.player_group.update()
            self.enemy_group.update()
        else:
            self.reset_sprite_groups()

        if self.player.health <= 0:
            self.player.lives -= 1
            if self.player.lives <= 0:
                State.push_screen(
                    GameOverScreen(
                        TileMap.width*TileMap.BLOCK_SIZE[0], 
                        TileMap.height*TileMap.BLOCK_SIZE[1]
                    )
                )
            else:
                self.tileMap.set_tile(self.player, 0, 0)
                self.player.health = self.player.std_health
                self.player.coords = (5, 5)
                self.reset_sprite_groups()

    def handle_keyboard(self, events):
        '''
        Function to handle the keyboard events and act accordingly

        @param events - The list of events from the game
        '''

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
                    State.push_screen(PauseScreen(self.player, self.tileMap))
                if event.key == K_i:
                    State.push_screen(InventoryScreen(self.player))

            if event.key in self.keyboard_input:
                (old_val, new_val) = self.keyboard_input[event.key]
                self.keyboard_input[event.key] = (new_val, event.type)


    def check_collisions(self):
        '''
        Checks the collisions between each of the sprite groups and removes them if health is 0 
        '''

        player_crate_collisions = pygame.sprite.spritecollide(self.player, self.crate_group, False, self.did_player_crate_collide)
        player_button_collisions = pygame.sprite.spritecollide(self.player, self.button_group, False, self.did_player_button_collide)
        player_gate_collisions = pygame.sprite.spritecollide(self.player, self.gate_group, False, self.did_player_gate_collide)
        player_enemy_collisions = pygame.sprite.spritecollide(self.player, self.enemy_group, False, self.player_enemy_collide)

        for bullet in self.bullet_group:
            collisions = pygame.sprite.spritecollide(bullet, self.crate_group, False, self.did_bullet_collide)
            for crate in collisions:
                self.bullet_group.remove(bullet)
            collisions = pygame.sprite.spritecollide(bullet, self.enemy_group, False, self.did_bullet_collide)
            for enemy in collisions:
                self.bullet_group.remove(bullet)
                if enemy.health <= 0:
                    self.player.increment_count()
                    self.enemy_group.remove(enemy)
                    try:
                        self.tileMap.tile.enemies.remove(enemy)
                    except ValueError:
                        try:
                            self.tileMap.tile.shooters.remove(enemy)
                            self.shooters.remove(enemy)
                        except ValueError:
                            self.tileMap.tile.bosses.remove(enemy)
                            self.victory()
            (x, y) = bullet.coords
            if y < 0 or y > TileMap.height - 1: 
                self.bullet_group.remove(bullet)
            if x < 0 or x > TileMap.width - 1: 
                self.bullet_group.remove(bullet)

        for bullet in self.enemy_bullet_group:
            collisions = pygame.sprite.spritecollide(bullet, self.crate_group, False)
            for crate in collisions:
                self.enemy_bullet_group.remove(bullet)
            collisions = pygame.sprite.spritecollide(bullet, self.player_group, False)
            if collisions:
                self.enemy_bullet_group.remove(bullet)
                self.player.takeHit(1)
            (x, y) = bullet.coords
            if y < 0 or y > TileMap.height - 1: 
                self.enemy_bullet_group.remove(bullet)
            if x < 0 or x > TileMap.width - 1: 
                self.enemy_bullet_group.remove(bullet)

    def player_enemy_collide(self, player, enemy):
        '''
        Function to test if a player and enemy have collided

        @param player - The player sprite
        @param enemy - The enemy that might have collided with the player
        '''
        if player.coords == enemy.coords:
            self.player.takeHit(1)
            self.throwBack(player, enemy.direction)
            return True
        else:
            return False

    def throwBack(self, entity, direction):
        '''
        Throws the player/enemy back if they collide with each other

        @param entity - The entity to be thrown back
        @param direction - The direction the entity will be thrown

        '''
        (ox, oy) = entity.coords
        entity.move(direction, self.tileMap.tile)
        (x, y) = entity.coords
        entity.isOutOfBounds(
            TileMap.width, 
            TileMap.height, 
            TileMap.TILE_LEFT, 
            TileMap.TILE_RIGHT, 
            TileMap.TILE_UP, 
            TileMap.TILE_DOWN
        )
        (px, py) = entity.coords
        if (px, py) != (x, y):
            entity.coords = (ox, oy)
            oppDir = self.oppositeDirection(direction)
            entity.move(oppDir, self.tileMap.tile)
            entity.move(oppDir, self.tileMap.tile)
        else:
            entity.move(direction, self.tileMap.tile)
            entity.isOutOfBounds(
                TileMap.width, 
                TileMap.height, 
                TileMap.TILE_LEFT, 
                TileMap.TILE_RIGHT, 
                TileMap.TILE_UP, 
                TileMap.TILE_DOWN
            )

    def oppositeDirection(self, direction):
        '''
        Changes the direction to the opposite one

        @param direction - The direction currently being faced
        '''
        if direction == Direction.up: 
            return Direction.down
        elif direction == Direction.down: 
            return Direction.up
        elif direction == Direction.left: 
            return Direction.right
        else: 
            return Direction.left

    def did_player_crate_collide(self, player_sprite, crate_sprite):
        '''
        Checks to see if a player and crate have collided and if it has an item in it
        it will be collected

        @param player_sprite - The player's sprite
        @param crate_sprite - The crate's sprite
        '''
        if player_sprite.coords == crate_sprite.coords:
            crate_sprite.takeHit(1)
            self.player.takeItem(crate_sprite)
            return True
        else:
            return False

    def did_bullet_collide(self, sprite_one, crate_sprite):
        '''
        Checks to see if a bullet collided with a crate

        @param sprite_one - The bullet's sprite 
        @param crate_sprite - The crate's sprite
        '''
        if sprite_one.coords == crate_sprite.coords:
            crate_sprite.takeHit(self.player.laser)
            return True
        else: 
            return False

    def did_player_button_collide(self, player_sprite, button_sprite):
        '''
        Checks to see if the button and player have collided

        @param player_sprite - The player's sprite
        @param button_sprite - THe button's sprite
        '''
        if player_sprite.coords == button_sprite.coords:
            if self.boss:
                self.enemy_group.remove(self.boss[0])
            self.shooters = []
            self.victory()
            return True
        else:
            return False

    def did_player_gate_collide(self, player_sprite, gate_sprite):
        '''
        Checks to see if player and gate have collided

        @param player_sprite - The player's sprite
        @param gate_sprite - The gate's sprite
        '''
        if player_sprite.coords == gate_sprite.coords:
            self.throwBack(player_sprite, self.oppositeDirection(player_sprite.direction))
            return True
        else:
            return False

    def victory(self):
        '''
        Once the victory condition has been met, it will push the victory screen to state
        '''
        State.push_screen(
            VictoryScreen(
                TileMap.width*TileMap.BLOCK_SIZE[0], 
                TileMap.height*TileMap.BLOCK_SIZE[1]
            )
        )

