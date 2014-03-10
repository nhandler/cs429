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

pygame.init()
height = 10
width = 10
BLOCK_SIZE = 60
screen = pygame.display.set_mode((width*BLOCK_SIZE, height*BLOCK_SIZE))
clock = pygame.time.Clock()
BLACK = (0,0,0)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BLACK)
crates = [
    ObjectSprite((1, 1)),
    ObjectSprite((5, 7)),
    ObjectSprite((2, 3)),
    ObjectSprite((9, 5)),
    ObjectSprite((9, 2)),
    ObjectSprite((3, 6)),
    ObjectSprite((7, 4)),
    ObjectSprite((8, 8)),
]

crate_group = pygame.sprite.RenderPlain(*crates)
player = PlayerSprite('Hero.png', (5, 5))
enemies = [
    EnemySprite("enemy.png", (7, 7)),
    EnemySprite("enemy.png", (3, 3))
]

player_group = pygame.sprite.RenderPlain(player)
enemy_group = pygame.sprite.RenderPlain(*enemies)
bullet_group = pygame.sprite.Group()

def did_crate_collide(sprite_one, crate_sprite):
    if sprite_one.coords == crate_sprite.coords:
        crate_sprite.takeHit()
        return True
    else: 
        return False

screen.blit(background, (0, 0))
pygame.display.flip()

tileMap = TileMap("../../maps/main_map.json")

player_group.update()
enemy_group.update()

can_fire = True
def fire():
    if can_fire:
        bullet = BulletSprite('bullet.png', player.coords, player.direction)
        bullet_group.add(bullet)

keyboard_input = {
    K_a: (KEYUP, KEYUP),
    K_d: (KEYUP, KEYUP),
    K_l: (KEYUP, KEYUP),
    K_s: (KEYUP, KEYUP),
    K_w: (KEYUP, KEYUP)
}

def takeHit():
    if State.health > 0:
        State.health -= 1
    if State.health == 0:
        sys.exit(0)

def main():
    while 1:
        global keyboard_input
        # Refresh keyboard state
        keyboard_input = {
            key: (new_val, new_val) 
            for key, (old_val, new_val) 
            in keyboard_input.items()
        }
        
        for event in pygame.event.get():
            if not hasattr(event, 'key'): 
                continue
            if event.key == K_ESCAPE: 
                sys.exit(0)
            elif event.type == KEYDOWN:
                if event.key == K_p:
                    State.paused = not State.paused
                if not State.paused:
                    if event.key == K_l:
                        fire()
                        can_fire = False
                    if event.key == K_h:
                        takeHit()

            elif event.type == KEYUP:
                if not State.paused:
                    if event.key == K_l: 
                        can_fire = True


            # If a key was pressed or released, update its value
            if event.key in keyboard_input:
                (old_val, new_val) = keyboard_input[event.key]
                keyboard_input[event.key] = (new_val, event.type)

        player.handle_input(keyboard_input)

        for enemy in enemy_group:
            enemy.act()

        for bullet in bullet_group:
            collisions = pygame.sprite.spritecollide(bullet, crate_group, False, did_crate_collide)
            for crate in collisions:
                bullet_group.remove(bullet)
            collisions = pygame.sprite.spritecollide(bullet, enemy_group, False, did_crate_collide)
            for enemy in collisions:
                bullet_group.remove(bullet)
                if enemy.health <= 0:
                    enemy_group.remove(enemy)
            (x, y) = bullet.coords
            if y < 0 or y > TileMap.height - 1: bullet_group.remove(bullet)
            if x < 0 or x > TileMap.width - 1: bullet_group.remove(bullet)


        if(tileMap.update(player, enemy_group)):
            bullet_group.update()
            player_group.update()
            enemy_group.update()

        if not State.paused:
            tileMap.draw(screen)
            crate_group.draw(screen)
            bullet_group.draw(screen)
            player_group.draw(screen)
            enemy_group.draw(screen)
        else:
            monospace_font = pygame.font.SysFont('monospace', 15)
            screen.fill((0, 0, 0))
            title = monospace_font.render('Game Paused', 1, (255, 255, 0))
            health = monospace_font.render('Health: {0}'.format(State.health), 1, (255, 255, 0))
            screen.blit(title, (100, 100))
            screen.blit(health, (100, 110))

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
