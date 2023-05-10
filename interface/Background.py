import pygame
# 背景类
class Background():
    def __init__(self,bgSurface):
        # 图片加载
        self.image = bgSurface
        # 设置位置
        self.rect = self.image.get_rect()
        self.rect.x = 0
        self.rect.y = 280
    
    def draw(self,windowSurface):
        self.rect.x -= 5
        print(self.rect.x)
        windowSurface.fill((255,255,255))
        windowSurface.blit(self.image,self.rect)