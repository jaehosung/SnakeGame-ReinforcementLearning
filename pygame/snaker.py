#####################################################################
#
#
#
#  SNAKER.py  - A simple SNAKE game written in Python and Pygame
#
#  This is my first Python / Pygame game written as a learning
#  exercise.
#
#
#  Version: 0.1
#  Date:  24 August 2008
#  Author:  R Brooks
#  Author email:  rsbrooks@gmail.com
#
#
#
#####################################################################



######### IMPORTS ###################################################


import random, math, pygame
from pygame.locals import *


counter = 0


    

######### MAIN #####################################################

def main():

    showstartscreen = 1
    
    while 1:
        ######## CONSTANTS

        WINSIZE = [200,200]

        WHITE = [255,255,255]
        BLACK = [0,0,0]
        RED = [255,0,0]
        GREEN = [0,255,0]


        BLOCKSIZE = [20,20]

        UP = 1
        DOWN = 3
        RIGHT = 2
        LEFT = 4

        MAXX = WINSIZE[0]
        MINX = 0
        MAXY = WINSIZE[1]
        MINY = 0

        SNAKESTEP = 20

        X_apple = WINSIZE[0]/SNAKESTEP
        Y_apple = WINSIZE[1]/SNAKESTEP

        TRUE = 1
        FALSE = 0


        ######## VARIABLES

        direction = RIGHT # 1=up,2=right,3=down,4=left
        snakexy = [0,WINSIZE[1]/2]
        snakelist = [[300,400],[280,400],[260,400]]
        counter = 0
        score = 0
        appleonscreen = 0
        #applexy = [0,0]
        newdirection = RIGHT
        snakedead = FALSE
        gameregulator = 6
        gamepaused = 0
        growsnake = 0  # added to grow tail by two each time
        snakegrowunit = 2 # added to grow tail by two each time



        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode(WINSIZE)
        pygame.display.set_caption('SNAKER')
        screen.fill(BLACK)

        while not snakedead:

            ###### get input events  ####

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()

            pressed_keys = pygame.key.get_pressed()

            if pressed_keys[K_LEFT]: newdirection = LEFT
            if pressed_keys[K_RIGHT]: newdirection = RIGHT
            if pressed_keys[K_UP]: newdirection = UP
            if pressed_keys[K_DOWN]: newdirection = DOWN
            if pressed_keys[K_q]: snakedead = TRUE



            #TODO Find the meanign of variable gameregulator
            if gameregulator == 6:

                ####### lets make sure we can't go back the reverse direction

                if newdirection == LEFT and not direction == RIGHT:
                    direction = newdirection

                elif newdirection == RIGHT and not direction == LEFT:
                    direction = newdirection

                elif newdirection == UP and not direction == DOWN:
                    direction = newdirection

                elif newdirection == DOWN and not direction == UP:
                    direction = newdirection

                ##### now lets move the snake according to the direction
                ##### if we hit the wall the snake dies
                ##### need to make it less twitchy when you hit the walls


                if direction == RIGHT:
                    snakexy[0] = snakexy[0] + SNAKESTEP
                    if snakexy[0] > MAXX:
                        snakedead = TRUE

                elif direction == LEFT:
                    snakexy[0] = snakexy[0] - SNAKESTEP
                    if snakexy[0] < MINX:
                        snakedead = TRUE

                elif direction == UP:
                    snakexy[1] = snakexy[1] - SNAKESTEP
                    if snakexy[1] < MINY:
                        snakedead = TRUE

                elif direction == DOWN:
                    snakexy[1] = snakexy[1] + SNAKESTEP
                    if snakexy[1] > MAXY:
                        snakedead = TRUE

                ### is the snake crossing over itself
                ### had to put the > 1 test in there as I was
                ### initially matching on first pass otherwise - not sure why

                if len(snakelist) > 3 and snakelist.count(snakexy) > 0:
                    snakedead = TRUE

                ###########################################################


                #### generate an apple at a random position if one is not on screen
                #### make sure apple never appears in snake position

                if appleonscreen == 0:
                    good = FALSE
                    while good == FALSE:
                        x = random.randrange(1,X_apple)
                        y = random.randrange(1,Y_apple)
                        applexy = [int(x*SNAKESTEP),int(y*SNAKESTEP)]
                        if snakelist.count(applexy) == 0:
                            good = TRUE
                    appleonscreen = 1

                #### add new position of snake head
                #### if we have eaten the apple don't pop the tail ( grow the snake )
                #### if we have not eaten an apple then pop the tail ( snake same size )

                snakelist.insert(0,list(snakexy))
                if snakexy[0] == applexy[0] and snakexy[1] == applexy[1]:
                    appleonscreen = 0
                    score = score + 1
                    growsnake = growsnake + 1
                elif growsnake > 0:
                    growsnake = growsnake + 1
                    if growsnake == snakegrowunit:
                        growsnake = 0
                else:
                    snakelist.pop()



                gameregulator = 0


            ###### RENDER THE SCREEN ###############

            ###### Clear the screen
            screen.fill(BLACK)
                  ###### Output the array elements to the screen as rectangles ( the snake)
            for element in snakelist:
                pygame.draw.rect(screen,RED,Rect(element,BLOCKSIZE))

            ###### Draw the apple
            pygame.draw.rect(screen,GREEN,Rect(applexy,BLOCKSIZE))

            ###### Flip the screen to display everything we just changed
            pygame.display.flip()



            gameregulator = gameregulator + 1

            clock.tick(100)



if __name__ == '__main__':
    main()



