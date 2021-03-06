# ICS3U
# Assignment 2: Logo
# <Ahmed M>

# adapted from http://www.101computing.net/getting-started-with-pygame/

# Import the pygame library and initialise the game engine
import pygame
pygame.init()

# Define some colours
# Colours are defined using RGB values
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (240, 0, 0)
LBLUE = (157, 186, 232) #Light Blue, Background

# Set the screen size (please don't change this)
SCREENWIDTH = 852
SCREENHEIGHT = 480

# Open a new window
# The window is defined as (width, height), measured in pixels
size = (SCREENWIDTH, SCREENHEIGHT)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Ahmed M's Target Logo")

# This loop will continue until the user exits the game
carryOn = True

# The clock will be used to control how fast the screen updates
clock = pygame.time.Clock()

#---------Main Program Loop----------
while carryOn:
    # --- Main event loop ---
    for event in pygame.event.get(): # Player did something
        if event.type == pygame.QUIT: # Player clicked close button
            carryOn = False

    # --- Game logic goes here
    # There should be none for a static image
    
    # --- Draw code goes here

    # Clear the screen to white
    screen.fill(LBLUE)

    # Queue different shapes and lines to be drawn
    #pygame.draw.ellipse(screen, RED, [50, 50, 300, 300], 0)
    #pygame.draw.ellipse(screen, WHITE, [100, 100, 200, 200], 0)
    #pygame.draw.ellipse(screen, RED, [150, 150, 100, 100], 0)

    pygame.draw.ellipse(screen, RED, [0, 0, 400, 400], 0) #Large Red Outside Circle
    pygame.draw.ellipse(screen, WHITE, [62.5, 62.5, 275, 275], 0) #Medium White Middle Circle
    pygame.draw.ellipse(screen, RED, [125, 125, 150, 150], 0) #Small Red Central Circle 
    
    

    # Update the screen with queued shapes
    pygame.display.flip()

    # --- Limit to 60 frames per second
    clock.tick(60)

# Once the main program loop is exited, stop the game engine
pygame.quit()
