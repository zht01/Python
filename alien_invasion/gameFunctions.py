import sys
import pygame


def checkEvent(ship):
    for event in pygame.event.get():
        if(event.type == pygame.QUIT):
            sys.exit()

        #控制ship左右上下移动
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                ship.moving_Horizontal = 1
            elif event.key == pygame.K_LEFT:
                ship.moving_Horizontal = -1
            elif event.key == pygame.K_DOWN:
                ship.moving_Vertical = 1
            elif event.key == pygame.K_UP:
                ship.moving_Vertical = -1
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                ship.moving_Vertical = 0
            elif event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT:
                ship.moving_Horizontal = 0


def updateScreen(aiSettings, screen, ship):
    screen.fill(aiSettings.screen_bgColor)
    ship.blitme()
    pygame.display.flip()