##########################
###Breakout Project#######
######By: William#########
##########################

import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

size = (950,650)
screen = pygame.display.set_mode(size)


#FUNCTIONS GO HERE
def paddle(x):
    pygame.draw.rect(screen, WHITE, [x, 600, 100, 10])

def blocks(x,y):
    pygame.draw.rect(screen, WHITE, [x, y, 50, 40])

def ball(x,y):
    pygame.draw.ellipse(screen, WHITE, [x, y, 15, 15])

def texts(score,location_x,location_y,text,colour,size):
   font=pygame.font.Font(None,size)
   scoretext=font.render(text+str(score), 1,colour)
   screen.blit(scoretext, (location_x, location_y))
   

def main():
    pygame.init()
    pygame.display.set_caption("Breakout")


    done = False
    start = False
    first = False
    once = True
    hit = False
    last = False
    win = False
    
    clock = pygame.time.Clock()

    #Making the block list
    block_list = []
    blocklist_y = [10,100,180,260,340]
    blocklist_x = [10,70,130,190,250,310,370,430,490,550,610,670,730]
    for i in blocklist_y:
        for q in blocklist_x:
            block = [q,i]
            block_list.append(block)
            

    paddle_xspeed = 0
    x_speed =  0
    y_speed = 0
     

    paddle_xcoord = 360
    x_coord = 0
    y_coord = 580
    
    lives = 3
    score = 0

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
        
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    paddle_xspeed = -10
                elif event.key == pygame.K_RIGHT:
                    paddle_xspeed = 10

                if start == False:
                    if event.key == pygame.K_SPACE:
                        y_speed = -5
                        start = True
     
            # User let up on a key
            elif event.type == pygame.KEYUP:
                # If it is an arrow key, reset vector back to zero
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    paddle_xspeed = 0

     

             
        paddle_xcoord += paddle_xspeed





                
        if start == False:
            x_coord = paddle_xcoord + 40
            y_coord = 580

        #For the paddle
        if paddle_xcoord <= 0:
            paddle_xcoord = 0

        elif paddle_xcoord >= 700:
            paddle_xcoord = 700

        #For the ball
        if y_coord <= 0:
            y_speed = -y_speed
            first = True

        elif x_coord <= 0:
            x_speed = -x_speed
            first = True
        elif x_coord+15 >= 800:
            x_speed = -x_speed
            first = True

        #Checking for game over
        if last == True:
            if y_coord+15 >= 650:
                texts('',400,205,"GAME OVER",WHITE,80)
                
        #Resetting
        if lives > 0 :   
            if y_coord+15 >= 650:
                start = False
                first = False
                once = True
                lives -= 1
                y_speed = 0
                x_speed = 0
                

         #dectating if hit paddle
        #For the sides
        if (y_coord <= 600 + 1) and (y_coord + 15 >= 600):
            if(x_coord + 15 >= paddle_xcoord) and (x_coord <= paddle_xcoord + 100):
                y_speed = -y_speed
                first = True

        elif (y_coord <= 600 + 10) and (y_coord + 15 >= 600):
            if(x_coord + 15 >= paddle_xcoord) and (x_coord <= paddle_xcoord + 100):
                x_speed = -x_speed
                first = True
                
        


        #Dectating if hit block
        first_fail = True
        #Bottom side
        for coord in (block_list):
            if (y_coord + 15 >= coord[1] + 40) and (y_coord <= coord[1] + 40):
                if (x_coord + 15 >= coord[0]) and (x_coord <= coord[0] + 50):
                    y_speed = -y_speed
                    first = True
                    hit = True
                    block_list.remove(coord)
                    score += 10

            #Top side
            elif (y_coord <= coord[1] + 1) and (y_coord + 15 >= coord[1]):
                if (x_coord + 15 >= coord[0]) and (x_coord <= coord[0] + 50):
                    y_speed = -y_speed
                    first = True
                    hit = True
                    block_list.remove(coord)
                    score += 10


            #Side side
            elif (y_coord <= coord[1] + 40) and (y_coord + 15 >= coord[1]):
                if (x_coord + 15 >= coord[0]) and (x_coord <= coord[0] + 50):
                    x_speed = -x_speed
                    first = True
                    hit = True
                    block_list.remove(coord)
                    score += 10


        #To make the vertical become horizontal after first bounce
        if once == True:
            if first == True:
                x_speed = -5
                once = False
                



        x_coord += x_speed
        y_coord += y_speed
        screen.fill(BLACK)

        #drawing paddles
        paddle(paddle_xcoord)

##        font = pygame.font.SysFont('Calibri', 25, True, False)
##        text = font.render(score, True, WHITE)
##        screen.blit(text, [250, 250])
        
        pygame.draw.rect(screen, WHITE, [800, 0, 400, 700])


            
        #Drawing blocks
        for coord in (block_list):
            blocks(coord[0],coord[1])

        #Drawing ball
        ball(x_coord,y_coord)

        texts(score,820,125,"Score:",BLACK,40)

        texts(lives,820,160,"Lives:",BLACK,40)

        #Checking for game over
        if score >= 650:
            texts('',150,230,"CONGRULATION",BLUE,100)
            win = True
            
        elif last == True:
            if win == False:
                if y_coord+15 >= 650:
                    texts('',200,230,"GAME OVER",RED,100)

        elif lives == 0:
            last = True
        
        pygame.display.flip()

        clock.tick(60)

    pygame.quit()


main()

