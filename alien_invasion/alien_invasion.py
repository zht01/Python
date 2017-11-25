import sys
import pygame
import gameFunctions as gf
import time
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
        gf.checkEvent(ship)
        ship.update()
        gf.updateScreen(ai_settings,screen, ship)
        time.sleep(0.01)

run_game()
