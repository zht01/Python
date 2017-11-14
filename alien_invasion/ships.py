import pygame


class Ship():
    def __init__(self, screen):
        self.screen = screen
        self.ShipImage = pygame.image.load('C:\\Users\\zhonghantian\\Desktop\\aeroplane-147495_640.bmp')
        self.ShipRect = self.ShipImage.get_rect()
        self.screenRect = screen.get_rect()

        self.ShipRect.centerx = self.screenRect.centerx
        self.ShipRect.bottom = self.screenRect.bottom

    def bliteme(self):
        self.screen.blit(self.ShipImage, self.ShipRect)