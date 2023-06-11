import pygame
# 重启按钮
class RestartInterface():
    def __init__(self,restartImage):
        self.image = restartImage
        self.rect = self.image.get_rect()
        self.rect.x = 420
        self.rect.y = 160

    def draw(self,windowSurface):
        windowSurface.blit(self.image,self.rect)