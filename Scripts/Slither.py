import pygame

pygame.init()

black = (0,0,0)
white = (255,255,255)
maroon = (128,0,0)

gameDisplay = pygame.display.set_mode((800,600))
pygame.display.set_caption('Slither')



gameExit = False

lead_x=300
lead_y=300
lead_x_change = 0
lead_y_change = 0
apple_x = 100
apple_y = 100

clock = pygame.time.Clock()



while not gameExit:
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            gameExit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                lead_x_change = -10
                lead_y_change = 0 #REM
            if event.key == pygame.K_RIGHT:
                lead_x_change = 10
                lead_y_change = 0 #REM
            if event.key == pygame.K_UP:
                lead_y_change = -10
                lead_x_change = 0 #REM
            if event.key == pygame.K_DOWN:
                lead_y_change = 10
                lead_x_change = 0 #REM
            if event.key == pygame.K_ESCAPE: # THIS MAKES THE GAME CLOSE WITH ESCAPE. :)
                gameExit = True
# FOR MAKING THE SNAKE GO TILL U RELEASE THE KEY REMOVE THE QUOTATIONS BELOW. AND REMOVE THE *ENTIRE LINES* WITH #REM ABOVE. :)
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
        pygame.draw.rect(gameDisplay , white, [apple_x,apple_y,10,10])
    pygame.display.update()
    clock.tick(15)
    



pygame.quit()
quit()
    
