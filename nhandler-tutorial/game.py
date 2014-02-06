import os, sys
from random import choice, randint, uniform
from math import sin, cos, radians

import pygame
from pygame import Rect, Color
from pygame.sprite import Sprite

from creep import Creep
from vec2d import vec2d
from simpleanimation import SimpleAnimation

def run_game():
    # Game parameters
    SCREEN_WIDTH, SCREEN_HEIGHT = 500, 400
    FIELD_RECT = Rect(50, 50, 300, 300)
    MESSAGE_RECT = Rect(360, 50, 130, 50)
    BG_TILE_IMG = 'images/brick_tile.png'

    CREEP_FILENAMES = [
        'images/bluecreep.png',
        'images/pinkcreep.png',
        'images/graycreep.png',
    ]
    N_CREEPS = 3
    CREEP_SPEED = 0.05    # 0.05 px/ms or 50 pixels per second
    
    pygame.init()
    screen = pygame.display.set_mode(
        (SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)
    clock = pygame.time.Clock()
    paused = False

    creep_images = [
        pygame.image.load(filename).convert_alpha()
            for filename in CREEP_FILENAMES]

    explosion_img = pygame.image.load('images/explosion1.png').convert_alpha()
    explosion_images = [
        explosion_img, pygame.transform.rotate(explosion_img, 90)]

    bg_tile_img = pygame.image.load(BG_TILE_IMG).convert_alpha()
    
    # Create N_CREEPS random creeps
    creeps = pygame.sprite.Group()
    for i in range(N_CREEPS):
        creeps.add(
            Creep(  screen=screen,
                    creep_image=choice(creep_images),
                    explosion_images=explosion_images,
                    field=FIELD_RECT,
                    init_position=( randint(FIELD_RECT.left,
                                            FIELD_RECT.right),
                                    randint(FIELD_RECT.top,
                                            FIELD_RECT.bottom)),
                    init_direction=(choice([-1, 1]),
                                    choice([-1, 1])),
                    speed=CREEP_SPEED))
    # The main game loop
    while True:
        # Limit frame speed to 50 FPS
        time_passed = clock.tick(50)
    
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    paused = not paused
            elif (  event.type == pygame.MOUSEBUTTONDOWN and
                    pygame.mouse.get_pressed()[0]):
                for creep in creeps:
                    creep.mouse_click_event(pygame.mouse.get_pos())

        if not paused:    
            # Redraw the background
            draw_background(screen, bg_tile_img, FIELD_RECT)

            msg1 = 'Creeps: %d' % len(creeps)
            msg2 = 'You won!' if len(creeps) == 0 else ''
            draw_messageboard(screen, MESSAGE_RECT, msg1, msg2)

            # Update and redraw all creeps
            for creep in creeps:
                creep.update(time_passed)
                creep.draw()
    
        pygame.display.flip()

def exit_game():
    sys.exit()

def draw_background(screen, tile_img, field_rect):
    img_rect = tile_img.get_rect()

    nrows = int(screen.get_height() / img_rect.height) + 1
    ncols = int(screen.get_width() / img_rect.width) + 1

    for y in range(nrows):
        for x in range(ncols):
            img_rect.topleft = (x * img_rect.width,
                                y * img_rect.height)
            screen.blit(tile_img, img_rect)

    field_color = (109, 41, 1)
    draw_rimmed_box(screen, field_rect, field_color, 4, Color('black'))

def draw_messageboard(screen, rect, message1, message2):
    draw_rimmed_box(screen, rect, (50, 20, 0), 4, Color('black'))

    my_font = pygame.font.SysFont('arial', 20)
    message1_sf = my_font.render(message1, True, Color('white'))
    message2_sf = my_font.render(message2, True, Color('white'))

    screen.blit(message1_sf, rect)
    screen.blit(message2_sf, rect.move(0, message1_sf.get_height()))

def draw_rimmed_box(screen, box_rect, box_color,
                    rim_width=0,
                    rim_color=Color('black')):
    """ Draw a rimmed box on the given surface. The rim is drawn
        outside the box rect.
    """
    if rim_width:
        rim_rect = Rect(box_rect.left - rim_width,
                        box_rect.top - rim_width,
                        box_rect.width + rim_width * 2,
                        box_rect.height + rim_width * 2)
        pygame.draw.rect(screen, rim_color, rim_rect)

run_game()
