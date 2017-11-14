import sys
import pygame
from pygame.locals import *
from settings import Settings
from ships import Ship

def run_game():
    # 初始pygame、设置初始值、获取屏幕对象
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))

    pygame.display.set_caption("Alient Invasion")

    ship = Ship(screen)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        screen.fill(ai_settings.screen_bgColor)
        ship.bliteme()
        pygame.display.flip()
run_game()
