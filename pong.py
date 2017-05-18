import pygame, sys
from pygame.locals import *

# Number of frames per second, change this to manipulate speed of the game
FPS = 200

# Global Variables to be used through our program
WINDOWWIDTH = 400
WINDOWSHEIGHT = 300

# Main function
def main():
    pygame.init()
    global DISPLAYSURF

    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWSWIDTH,WINDOWSHEIGHT))
    pygame.display.set_caption('Pong')

    while True: #main game loop
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()

        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__=='__main__':
    main()
