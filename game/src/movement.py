import pygame 
import math
import sys
from pygame.locals import *
from player import PlayerSprite, Direction, HorizontalMovement, VerticalMovement
from crate import ObjectSprite
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
]

crates_2 = [
    ObjectSprite((9, 2)),
    ObjectSprite((3, 6)),
    ObjectSprite((7, 4)),
    ObjectSprite((8, 8)),
]
crate_group = pygame.sprite.RenderPlain(*crates)
crate_group_2 = pygame.sprite.RenderPlain(*crates_2)
player = PlayerSprite('Hero.png', (5, 5))
player_group = pygame.sprite.RenderPlain(player)

def did_collide(sprite_one, sprite_two):
    if sprite_one.coords == sprite_two.coords: return True
    else: return False

def did_crate_collide(sprite_one, crate_sprite):
    if sprite_one.coords == crate_sprite.coords:
        crate_sprite.takeHit()
        return True
    else: 
        return False

screen.blit(background, (0, 0))
pygame.display.flip()

keydown_moves = { K_d : (player.changeHorizontalMovement, HorizontalMovement.right), K_a : (player.changeHorizontalMovement, HorizontalMovement.left), 
                  K_w : (player.changeVerticalMovement, VerticalMovement.up), K_s : (player.changeVerticalMovement, VerticalMovement.down)}

keyup_moves = { K_d : (player.changeHorizontalMovement, HorizontalMovement.none), K_a : (player.changeHorizontalMovement, HorizontalMovement.none), 
                K_w : (player.changeVerticalMovement, VerticalMovement.none), K_s : (player.changeVerticalMovement, VerticalMovement.none)}

tileMap = TileMap("../../maps/main_map.json")

player_group.update(10)

while 1:
    deltat = clock.tick(10)
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        if event.key == K_ESCAPE: sys.exit(0)
        elif event.type == KEYDOWN:
            (move, arg) = keydown_moves.get(event.key, (lambda arg: None, 0))
            move(arg)
            '''
            if event.key == K_d:
                player.horizontalMovement = HorizontalMovement.right
            elif event.key == K_a:
                player.horizontalMovement = HorizontalMovement.left
            elif event.key == K_w:
                player.verticalMovement = VerticalMovement.up
            elif event.key == K_s:
                player.verticalMovement = VerticalMovement.down
            '''
        elif event.type == KEYUP:
            (move, arg) = keyup_moves.get(event.key, (lambda arg: None, 0))
            move(arg)
            '''
            if event.key == K_d:
                player.horizontalMovement = HorizontalMovement.none
            elif event.key == K_a:
                player.horizontalMovement = HorizontalMovement.none
            elif event.key == K_w:
                player.verticalMovement = VerticalMovement.none
            elif event.key == K_s:
                player.verticalMovement = VerticalMovement.none
            '''

    collisions = pygame.sprite.spritecollide(player, crate_group, False, did_crate_collide)
    collide = pygame.sprite.spritecollide(player, crate_group_2, True, did_collide)
    #crate_group.update(collisions)
    
    #screen.blit(background, (0, 0))
    
    if(tileMap.update(deltat, player)):
        player_group.update(deltat)
    tileMap.draw(screen)
    crate_group.draw(screen)
    crate_group_2.draw(screen)
    player_group.draw(screen)
    
    pygame.display.flip()
    
