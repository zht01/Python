import pygame


class Ship():
    """函数描述：初始化飞船相关参数:图片、位置、飞船运动情况
    参数：self：固定的格式，类的初始化
    screen:窗口屏幕
    """
    def __init__(self, screen):

        self.screen = screen
        # 飞船图片
        self.shipImage = pygame.image.load('Images\\Avion_Aircraft.png')
        self.shipRect = self.shipImage.get_rect()
        self.screenRect = screen.get_rect()
        # 飞船位置
        self.shipRect.centerx = self.screenRect.centerx
        self.shipRect.bottom = self.screenRect.bottom

        # 飞船水平、垂直运动
        self.moving_Horizontal = 0  # 0：不动；1：向右；-1：向左
        self.moving_Vertical = 0  # 0：不动；1：向下；-1：向上

    """图片显示在相应位置"""
    def blitme(self):
        self.screen.blit(self.shipImage, self.shipRect)

    """更新飞船位置"""
    def update(self):
        if self.moving_Horizontal == 0:
            self.shipRect.centerx += 0
        elif self.moving_Horizontal == 1 and self.shipRect.right < self.screenRect.right:
            self.shipRect.centerx += 1
        elif self.moving_Horizontal == -1 and self.shipRect.left > 0:
            self.shipRect.centerx -= 1

        if self.moving_Vertical == 0:
            self.shipRect.centery += 0
        elif self.moving_Vertical == 1:
            self.shipRect.centery += 1
        elif self.moving_Vertical == -1:
            self.shipRect.centery -= 1
