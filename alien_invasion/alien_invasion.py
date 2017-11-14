import sys
import pygame
from pygame.locals import *
from settings import Settings

pygame.display.set_mode((50,50))
def run_game():
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alient Invasion")
    while(True):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        pygame.display.flip()
run_game()
