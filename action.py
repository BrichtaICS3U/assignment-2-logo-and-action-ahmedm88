# ICS3U
# Assignment 2: Action
# <Ahmed M>

# adapted from http://www.101computing.net/getting-started-with-pygame/
# background image taken from https://www.google.ca/search?q=night+background&safe=strict&rlz=1C1GGRV_enCA782CA782&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjblY3SqcHaAhUo34MKHQQ_BYwQ_AUICigB&biw=1440&bih=794#imgdii=hBKqiS1TmbCbeM:&imgrc=px-7QX_SYTwDsM:
# Import the pygame library and initialise the game engine
# Don't forget to import your class
import pygame, random
from Planet import Planets
pygame.init()
background = pygame.image.load("image.jpg")
# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

speed = 2
# Set the screen size
SCREENWIDTH = 800
SCREENHEIGHT = 569

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
<<<<<<< HEAD
pygame.display.set_caption("Ahmed M's Animation")

all_sprites_list = pygame.sprite.Group()

playerPlanet = Planets(GREEN, 60, 80, 70)
playerPlanet.rect.x = 400
playerPlanet.rect.y = 235

planets1 = Planets(BLUE, 60, 80, random.randint(50,100))
planets1.rect.x = 600
planets1.rect.y = 200
=======
pygame.display.set_caption("Ahmed M's animation")
>>>>>>> 1c75e4c17cbdc6e69c13d3428149341db476cb13

planets2 = Planets(RED, 60, 80, random.randint(50,100))
planets2.rect.x = 200
planets2.rect.y = 200

all_sprites_list.add(playerPlanet)
all_sprites_list.add(planets1)
all_sprites_list.add(planets2)

all_coming_planets = pygame.sprite.Group()
all_coming_planets.add(planets1)
all_coming_planets.add(planets2)
# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
screen.blit(background, (0, 0))
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False


        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            playerPlanet.moveLeft(5)
        if keys[pygame.K_RIGHT]:
            playerPlanet.moveRight(5)
       
    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    #screen.fill(WHITE)

    # Queue different shapes and lines to be drawn
    # pygame.draw.rect(screen, RED, [55, 200, 100, 70], 0)
    # pygame.draw.line(screen, GREEN, [0, 0], [100, 100], 5)
    # pygame.draw.ellipse(screen, BLACK, [20, 20, 250, 100], 2)
    all_sprites_list.draw(screen)
    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

    if keys[pygame.K_SPACE]:
        carryOn = False
# Once the main program loop is exited, stop the game engine
pygame.quit()
