#The "Amazing Bario Cousins" program
#a side-scrolling 2D platform-based game inspired by the classic video game Super Mario Brothers
#Jason Yeung and Joey Chik
#created: 2017-05-25
#last edit: 2017-06-08

#import necessary modules
import pygame
from classes import *

def mainProgLoop():
    #initialize game engine
    pygame.init()

    #set screen
    size = (1300, 700)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Amazing Bario Cousins')

    level_list = []
    level_list.append(Level_01(player, screen))
    level_list.append(Level_02(player, screen))

    current_level_no = 0
    current_level = level_list[current_level_no]

    player.level = current_level

    #initialize clock
    clock = pygame.time.Clock()

    #initialize necessary variables
    kLeft = False
    kRight = False
    kUp = False

    kLeftTemp1 = False
    kRightTemp1 = False
    kUpTemp1 = False

    kLeftTemp2 = False
    kRightTemp2 = False
    kUpTemp2 = False

    #loop until user clicks close button
    done = False

    #run main menu
    MainMenu(screen, clock)

    while not done:
        #event processing
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            if not hasattr(event, 'key'): continue
            #the kXXXTemp variables represent the key being pressed and released
            #the kXXX variables will stay true as long as the key is being held down
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    kLeft = True
                    kLeftTemp1 = True
                if event.key == pygame.K_RIGHT:
                    kRight = True
                    kRightTemp1 = True
                if event.key == pygame.K_UP:
                    kUp = True
                    kUpTemp1 = True
                    player.jump()
                if event.key == pygame.K_p:
                    pause = True
                    Pause_screen(screen, clock)
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    kLeft = False
                    kLeftTemp2 = True
                if event.key == pygame.K_RIGHT:
                    kRight = False
                    kRightTemp2 = True
                if event.key == pygame.K_UP:
                    kUp = False
                    kUpTemp2 = False

        #move player
        player.update(kLeft, kRight, kLeftTemp1, kLeftTemp2, kRightTemp1, kRightTemp2)

        current_level.update(player.change_x)

        if current_level.worldShift < current_level.level_limit:
            if current_level_no < len(level_list)-1:
                player.rect.x = 120
                current_level_no += 1
                current_level = level_list[current_level_no]
                player.level = current_level
            else:
                # Out of levels. This just exits the program.
                # You'll want to do something better.
                done = True

        #reset temporary variables
        kLeftTemp1 = False
        kRightTemp1 = False

        kLeftTemp2 = False
        kRightTemp2 = False

        pause = False

        #graphics
        screen.fill(LIGHT_BLUE)
        current_level.draw()
        screen.blit(player.image, [player.rect.x, player.rect.y])

        #update display
        pygame.display.flip()

        #limit framerate
        clock.tick(60)
    pygame.quit()

mainProgLoop()
