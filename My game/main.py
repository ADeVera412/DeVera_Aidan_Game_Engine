# Code from Chris Bradfield tutorials content from kids can code: http://kidscancode.org/blog/
# https://github.com/kidscancode/pygame_tutorials/tree/master/platform 
# Code from Chris Cozort 

# GameDesign:
# Goals save the princess, don't fall off plats, reach final plat, avoid projectiles, collect stars, next level
# Rules jump and run, dont' fall, hit mob respawn, stay above zero health, 
# Feedback score at top of screen, sound effects, player damage animation
# Freedom Run side to side, jump

# Feature Goals:
#Add trophy to the game
#Have the mobs follow the player
 
# Have platforms scroll left when I move right, like Super Mario.
# Have obstacles that bounce the player backwards from the point of collision
# add a double jump


# import libraries and modules
import pygame as pg
from pygame.sprite import Sprite
import random
from random import randint
import os
from settings import *
from sprites import *
from sprites import Player
from math import floor

vec = pg.math.Vector2

# setup asset folders here - images sounds etc.
game_folder = os.path.dirname(__file__)
img_folder = os.path.join(game_folder, 'Game images')
snd_folder = os.path.join(game_folder, 'sounds')

class Cooldown():
    def __init__(self):
        self.current_time = 0
        self.event_time = 0
        self.delta = 0
        # ticking ensures the timer is counting...
    def ticking(self):
        self.current_time = floor((pg.time.get_ticks())/1000)
        self.delta = self.current_time - self.event_time
    def timer(self):
        self.current_time = floor((pg.time.get_ticks())/1000)

#Create a class to define the attributes of the game
class Game:
    def __init__(self):
        # init pygame and create a window
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode((WIDTH, HEIGHT))
        pg.display.set_caption("My Game...")
        self.clock = pg.time.Clock()
        self.running = True
        self.paused = False
        self.cd = Cooldown()
    
    #Instantiate and add the sprites to the game
    def new(self):
        # create a group for all sprites
        self.score = 0
        self.all_sprites = pg.sprite.Group()
        self.all_platforms = pg.sprite.Group()
        self.all_mobs = pg.sprite.Group()
        self.all_projectiles = pg.sprite.Group()
        # instantiate classes
        self.player = Player(self, pg.K_a, pg.K_d, pg.K_w, "theBigBell.png", 5, 4)
        self.trophy = Trophy(self, WIDTH/2, HEIGHT, "Trophy.png")
        # add instances to groups
        self.all_sprites.add(self.trophy)
        self.all_sprites.add(self.player)
        self.ground = Platform(*GROUND)
        self.all_sprites.add(self.ground)
        for p in PLATFORM_LIST:
            # instantiation of the Platform class
            plat = Platform(*p)
            self.all_sprites.add(plat)
            self.all_platforms.add(plat)

        for m in range(0,9):
            #Instantiation of the mobs
            m = Mob(self, randint(0, WIDTH), randint(0, HEIGHT/2), 20, 20, "normal")
            self.all_sprites.add(m)
            self.all_mobs.add(m)
        
        
    
        
        

        self.run()
    
    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            if not self.paused:
                self.update()
            self.draw()

    #Update the state of a sprite when a certain action happens
    def update(self):
        self.cd.ticking()
        # mhits = pg.sprite.spritecollide(self.player, self.all_mobs, False)
        # if mhits:
        #     print('this MOB collision happened in main')
        self.all_sprites.update()
        if self.player.pos.x < 0:
            self.player.pos.x = WIDTH
        if self.player.pos.x > WIDTH:
            self.player.pos.x = 0
        
        # this is what prevents the player from falling through the platform when falling down...
        if self.player.vel.y != 0:
            hits = pg.sprite.spritecollide(self.player, self.all_platforms, False)
            if hits:
                if self.player.vel.y > 0:
                    self.player.pos.y = hits[0].rect.top
                    self.player.vel.y = 0
                    self.player.vel.x = hits[0].speed*1.5
         # this prevents the player from jumping up through a platform
                elif self.player.vel.y <= 0:
                    if self.player.rect.top >= hits[0].rect.top - 5:    
                        self.player.vel.y = -self.player.vel.y
            ghits = pg.sprite.collide_rect(self.player, self.ground)
            if ghits:
                self.player.pos.y = self.ground.rect.top
                self.player.vel.y = 0
            '''
            if self.player2.vel.y > 0:
                hits = pg.sprite.spritecollide(self.player2, self.all_platforms, False)
                ghits = pg.sprite.collide_rect(self.player2, self.ground)
                if hits or ghits:
                    self.player2.pos.y = hits[0].rect.top
                    self.player2.vel.y = 0
                    self.player2.vel.x = hits[0].speed*1.5
                    '''
    def events(self):
        for event in pg.event.get():
        # check for closed window
            if event.type == pg.QUIT:
                if self.playing:
                    self.playing = False
                self.running = False
    ####################Draw #############################
    def draw(self):
        # draw the background screen
        self.screen.fill(RED)
        # draw all sprites
        self.all_sprites.draw(self.screen)
        self.draw_text("P1 - Health: " + str(self.player.health), 22, WHITE, WIDTH/2, HEIGHT/24)
        #self.draw_text("P2 - Health: " + str(self.player2.health), 22, WHITE, WIDTH/2, HEIGHT/10)
        self.draw_text("acc: " + str(self.player.acc.x), 22, WHITE, WIDTH/2, HEIGHT/6)
        # buffer - after drawing everything, flip display
        pg.display.flip()
    
    def draw_text(self, text, size, color, x, y):
        font_name = pg.font.match_font('arial')
        font = pg.font.Font(font_name, size)
        text_surface = font.render(text, True, color)
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x,y)
        self.screen.blit(text_surface, text_rect)

    def show_start_screen(self):
        pass
    def show_go_screen(self):
        pass

g = Game()
while g.running:
    g.new()


pg.quit()
