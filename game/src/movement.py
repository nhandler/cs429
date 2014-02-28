import pygame 
import math
import sys
from pygame.locals import *
from player import PlayerSprite, Direction, HorizontalMovement, VerticalMovement
from crate import ObjectSprite
from bullet import BulletSprite
from tileMap import *

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
player_group = pygame.sprite.RenderPlain(player)
bullet_group = pygame.sprite.Group()

def did_crate_collide(sprite_one, crate_sprite):
    if sprite_one.coords == crate_sprite.coords:
        crate_sprite.takeHit()
        return True
    else: 
        return False

screen.blit(background, (0, 0))
pygame.display.flip()

keydown_moves = { K_d : (player.changeHorizontalMovement, HorizontalMovement.right),
                  K_a : (player.changeHorizontalMovement, HorizontalMovement.left), 
                  K_w : (player.changeVerticalMovement, VerticalMovement.up),
                  K_s : (player.changeVerticalMovement, VerticalMovement.down)}

keyup_moves = { K_d : (player.changeHorizontalMovement, HorizontalMovement.none),
                K_a : (player.changeHorizontalMovement, HorizontalMovement.none), 
                K_w : (player.changeVerticalMovement, VerticalMovement.none),
                K_s : (player.changeVerticalMovement, VerticalMovement.none)}

tileMap = TileMap("../../maps/main_map.json")

player_group.update(10)

can_fire = True
def fire():
    if can_fire:
        bullet = BulletSprite('bullet.png', player.coords, player.direction)
        bullet_group.add(bullet)

while 1:
    deltat = clock.tick(10)
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        if event.key == K_ESCAPE: sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_l:
                fire()
                can_fire = False
            (move, arg) = keydown_moves.get(event.key, (lambda arg: None, 0))
            move(arg)
        elif event.type == KEYUP:
            if event.key == K_l: can_fire = True
            (move, arg) = keyup_moves.get(event.key, (lambda arg: None, 0))
            move(arg)

    for bullet in bullet_group:
        collisions = pygame.sprite.spritecollide(bullet, crate_group, False, did_crate_collide)
        for crate in collisions:
            bullet_group.remove(bullet)
        (x, y) = bullet.coords
        if y < 0 or y > TileMap.height - 1: bullet_group.remove(bullet)
        if x < 0 or x > TileMap.width - 1: bullet_group.remove(bullet)
        
    if(tileMap.update(deltat, player)):
        player_group.update(deltat)
        bullet_group.update(deltat)
    tileMap.draw(screen)
    crate_group.draw(screen)
    player_group.draw(screen)
    bullet_group.draw(screen)
    
    pygame.display.flip()
    
