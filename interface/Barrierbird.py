from typing import Any
import pygame
times = 0

class BarrierbirdInterface(pygame.sprite.Sprite):
    def __init__(self,  image_list, score):
        super().__init__()
        self.image_list = image_list
        self.image = self.image_list[0]
        # 速度
        self.speed = 14
        # 位置信息
        self.rect = self.image.get_rect()
        self.rect.x = 10000
        self.rect.y = 220.6
        # 增加遮罩
        self.mask = pygame.mask.from_surface(self.image)
        # 分数
        self.score = score

    def draw(self, windowSurface):
        global times
        if times == 28:
            times = 0
        image = self.image_list[times]
        windowSurface.blit(image, self.rect)
        times += 1

    def update(self):
        self.rect.x -= self.speed
# 鱼骨头
