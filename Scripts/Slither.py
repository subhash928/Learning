import pygame
import time

pygame.init()

black = (0,0,0)
white = (255,255,255)
maroon = (128,0,0)
red = (255,0,0)


gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')

clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 25)
def message_to_screen(msg,colour):
        screen_text = font.render(msg, True, colour)
        gameDisplay.blit(screen_text, [200,250])


def gameLoop ():
    gameExit = False
    gameOver = False

    lead_x=300
    lead_y=300
    lead_x_change = 0
    lead_y_change = 0
    apple_x = 100
    apple_y = 100




    while not gameExit:

        while gameOver == True:
            gameDisplay.fill(white)
            message_to_screen("UMMALA OTHA BADDE, Press C to play again or Q to quit",red)
            pygame.display.update()

            for event in pygame.event.get():
                print(event)
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                            gameExit = True
                            gameOver = False
                    if event.key == pygame.K_c:
                            gameLoop()

                            
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                gameExit = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -10
                    lead_y_change = 0 #REM
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = 10
                    lead_y_change = 0 #REM
                elif event.key == pygame.K_UP:
                    lead_y_change = -10
                    lead_x_change = 0 #REM
                elif event.key == pygame.K_DOWN:
                    lead_y_change = 10
                    lead_x_change = 0 #REM
                elif event.key == pygame.K_ESCAPE: # THIS MAKES THE GAME CLOSE WITH ESCAPE. :)
                    gameExit = True
    # FOR MAKING THE SNAKE GO TILL YOU RELEASE THE KEY REMOVE THE QUOTATIONS BELOW. AND REMOVE THE *ENTIRE LINES* WITH #REM ABOVE. :)
            """if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    lead_x_change = 0
                if event.key == pygame.K_RIGHT:
                    lead_x_change = 0
                if event.key == pygame.K_UP:
                    lead_y_change = 0
                if event.key == pygame.K_DOWN:
                    lead_y_change = 0"""
        lead_x += lead_x_change
        lead_y += lead_y_change
        gameDisplay.fill(white)
        pygame.draw.rect(gameDisplay, maroon, [apple_x,apple_y,10,10])
        pygame.draw.rect(gameDisplay, black, [lead_x,lead_y,10,10])
        pygame.display.update()
        if lead_x == apple_x and lead_y == apple_y:
            pygame.draw.rect(gameDisplay , white , [apple_x,apple_y,10,10])
        pygame.display.update()
        clock.tick(3)
        if lead_x >= 800 or lead_x <= 0 or lead_y <=0 or lead_y>=600:
            gameOver = True


    pygame.quit()
    quit()

gameLoop()
        

