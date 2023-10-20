#This file was created by Aidan DeVera on 10/18/23
#Content from Chris Bradfield; Kids can code
#KidsCanCode - Game Development with pygame video series


# game settings 
WIDTH = 360
HEIGHT = 480
FPS = 30
SCORE = 0


# Set a list of platforms that you want in your game
PLATFORM_LIST =  [(0, HEIGHT - 40, WIDTH, 40, "normal"),               
                  (WIDTH / 2 - 50, HEIGHT * 3 / 4, 100, 50, "normal"),
                  (200, HEIGHT - 350, 100, 50, "normal"),
                  (140, 200, 25, 30, "normal"),
                  (200, 50, 100, 20, "normal"),
                  (170, 100, 50, 25, "normal")]

# player settings
PLAYER_JUMP = 30
PLAYER_GRAV = 1.5

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
                   

