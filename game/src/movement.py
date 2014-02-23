import pygame, math, sys
from pygame.locals import *
from player import PlayerSprite
from crate import ObjectSprite

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

screen.blit(background, (0, 0))
pygame.display.flip()
while 1:
    deltat = clock.tick(10)
    for event in pygame.event.get():
        if not hasattr(event, 'key'): continue
        if event.key == K_ESCAPE: sys.exit(0)
        elif event.type == KEYDOWN:
            if event.key == K_d:
                player.right = True
                player.left = False
                #player.up = False
                #player.down = False
            elif event.key == K_a:
                player.left = True
                player.right = False
                #player.up = False
                #player.down = False
            elif event.key == K_w:
                player.up = True
                player.down = False
                #player.left = False
                #player.right = False
            elif event.key == K_s:
                player.down = True
                player.up = False
                #player.left = False
                #player.right = False
        elif event.type == KEYUP:
            if event.key == K_d:
                player.right = False
            elif event.key == K_a:
                player.left = False
            elif event.key == K_w:
                player.up = False
            elif event.key == K_s:
                player.down = False

    player_group.update(deltat)
    collisions = pygame.sprite.spritecollide(player, crate_group, False, did_collide)
    collide = pygame.sprite.spritecollide(player, crate_group_2, True, did_collide)
    crate_group.update(collisions)
    screen.blit(background, (0, 0))
    crate_group.draw(screen)
    crate_group_2.draw(screen)
    player_group.draw(screen)
    pygame.display.flip()