from typing import Any
import pygame
# 障碍类
class BarrierInterface(pygame.sprite.Sprite):
    def __init__(self,image,score):
        super().__init__()
        self.image = image
        # 速度
        self.speed = 10
        # 位置信息
        self.rect = self.image.get_rect()
        self.rect.x = 900
        if self.rect.height == 30:
            self.rect.y = 265
        else:
            self.rect.y = 240
        # 增加遮罩
        self.mask = pygame.mask.from_surface(self.image)
        # 分数
        self.score = score

    def draw(self,windowSurface):
        # 更新x
        windowSurface.blit(self.image,self.rect)

    def update(self):
        self.rect.x -= self.speed

