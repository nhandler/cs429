import pygame, math, sys
from pygame.locals import *
import spritesheet
from SpriteSheetAnim import SpriteStripAnim


height = 10
width = 10
BLOCK_SIZE = 60
screen = pygame.display.set_mode((width*BLOCK_SIZE, height*BLOCK_SIZE))
clock = pygame.time.Clock()
BLACK = (0,0,0)
background = pygame.Surface(screen.get_size())
background = background.convert()
background.fill(BLACK)

class PlayerSprite (pygame.sprite.Sprite):
    def __init__ (self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.src_image = pygame.image.load(image)
        self.coords = position
        self.position = (((self.coords[0] * BLOCK_SIZE) + (BLOCK_SIZE/2)), ((self.coords[1] * BLOCK_SIZE) + (BLOCK_SIZE/2)))
        self.up = self.down = self.right = self.left = False
        self.direction = "down"
        self.strips = self.imageStrips(self.src_image)
        self.currentStrip = self.strips[self.direction]
        self.image = self.currentStrip.next()
        self.rect_center = self.position

    def imageStrips(image, dummy):
        strips = dict()
        strips["up"] = SpriteStripAnim('Hero.png', (0,0,16,16), 4, 1, True, 4)
        strips["down"] = SpriteStripAnim('Hero.png', (16*4+1,0,16,16), 4, 1, True, 4)
        strips["right"] =  SpriteStripAnim('Hero.png', (16*4+1, 17, 16, 16), 4, 1, True, 4)
        strips["left"] = SpriteStripAnim('Hero.png', (0,17,16,16), 4, 1, True, 4)
        return strips

    def update (self, deltat):
        x, y = self.coords

        if self.up:
            y -= 1
            self.direction = "up"
            if self.currentStrip is self.strips[self.direction]:
                self.image = self.currentStrip.next()
                print "Right"
            else:
                self.currentStrip = self.strips[self.direction]
                self.image = self.currentStrip.next()
            #self.up = False
        if self.down:
            y += 1
            self.direction  = "down"
            if self.currentStrip is self.strips[self.direction]:
                print "Down"
                self.image = self.currentStrip.next()
            else:
                self.currentStrip = self.strips[self.direction]
                self.image = self.currentStrip.next()
            #self.down = False
        if self.left:
            x -= 1
            self.direction = "left"
            if self.currentStrip is self.strips[self.direction]:
                print "Left"
                self.image = self.currentStrip.next()
            else:
                self.currentStrip = self.strips[self.direction]
                self.image = self.currentStrip.next()
            #self.left = False
        if self.right:
            x += 1
            self.direction = "right"
            if self.currentStrip is self.strips[self.direction]:
                print "Right"
                self.image = self.currentStrip.next()
            else:
                self.currentStrip = self.strips[self.direction]
                self.image = self.currentStrip.next()
            #self.right = False

        if x < 0: x = 0
        if x > width - 1: x = width - 1
        if y < 0: y = 0
        if y > height - 1: y = height - 1

        self.coords = (x, y)
        self.position = (((x * BLOCK_SIZE) + (BLOCK_SIZE/2)), ((y * BLOCK_SIZE) + (BLOCK_SIZE/2)))
        self.rect = self.image.get_rect()
        self.currentStrip = self.strips[self.direction]
        self.rect.center = self.position

class ObjectSprite (pygame.sprite.Sprite):
    normal = pygame.image.load('crate.png')
    hit = pygame.image.load('burning_crate.png')

    def __init__ (self, position):
        pygame.sprite.Sprite.__init__(self)
        self.coords = position
        self.position = (((self.coords[0] * BLOCK_SIZE) + (BLOCK_SIZE/2)), ((self.coords[1] * BLOCK_SIZE) + (BLOCK_SIZE/2)))
        self.image = self.normal
        self.rect = self.image.get_rect()
        self.rect.center = self.position

    def update (self, hit_list):
        if self in hit_list:
            self.image = self.hit

        self.rect = self.image.get_rect()
        self.rect.center = self.position

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
