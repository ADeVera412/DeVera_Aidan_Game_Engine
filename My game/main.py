# This file was created by Aidan DeVera

# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *

vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'Game images')





def draw_text(text, size, color, x, y):
    font_name = pg.font.match_font('arial')
    font = pg.font.Font(font_name, size)
    text_surface = font.render(text, True, color)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x,y)
    self.screen.blit(text_surface, text_rect)



class Game:
    def __init__(self):
   # init pygame and create a window
    pg.init()
    pg.mixer.init()
    screen = pg.display.set_mode((WIDTH, HEIGHT))
    pg.display.set_caption("My Game...")
    self.clock = pg.time.Clock()
    self.running = True
    
    def new(self):
        # create a group for all sprites
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        # instantiate classes
        player = Player()
        # add instances to groups
        self.all_sprites.add(player)


    for p in PLATFORM_LIST:
        # Instantiation of the Platform class
        plat = Platform(*p)
        all_sprites.add(plat)
        all_platforms.add(plat)

    #Instantiation of mob class
    for m in range(0,25):
        m = Mob(randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20, "normal")
        all_sprites.add(m)
        all_mobs.add(m)
    
    def run(self):
        self.playing = True
    while self.playing:




# Game loop
running = True
while running:
    # keep the loop running using clock
    clock.tick(FPS)
        
    for event in pg.event.get():
        # check for closed window
        if event.type == pg.QUIT:
            running = False
    
    ############ Update ##############
    # update all sprites
    all_sprites.update()

    # this is what prevents the player from falling through the platform when falling down...
    if player.vel.y > 0:
            hits = pg.sprite.spritecollide(player, all_platforms, False)
            if hits:
                player.pos.y = hits[0].rect.top
                player.vel.y = 0
                
    # this prevents the player from jumping up through a platform
    if player.vel.y < 0:
        hits = pg.sprite.spritecollide(player, all_platforms, False)
        if hits:
            print("ouch")
            SCORE -= 1
            if player.rect.bottom >= hits[0].rect.top - 5:
                player.rect.top = hits[0].rect.bottom
                player.acc.y = 5
                player.vel.y = 0

    ############ Draw ################
    # draw the background screen
    self.screen.fill(BLACK)
    # draw all sprites
    self.all_sprites.draw(self.screen)
    draw_text("Score: " + str(SCORE), 22, WHITE, WIDTH/2, HEIGHT/10)

    # buffer - after drawing everything, flip display
    pg.display.flip()

pg.quit()
