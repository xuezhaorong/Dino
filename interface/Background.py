import pygame


# 背景类
class Background():
    def __init__(self, bgSurface):
        # 图片加载


        self.image1 = bgSurface
        self.image2 = bgSurface
        # 设置位置
        self.rect_1 = self.image1.get_rect()
        self.rect_1.left
        self.rect_1.bottom = 300

        self.rect_2 = self.image2.get_rect()
        self.rect_2.left
        self.rect_2.bottom = 300



    def draw(self, windowSurface):

        if self.rect_1.right < 0:
            self.rect_1.left = self.rect_1.right
        else:
            self.rect_1.left -= 5
        windowSurface.fill((255, 255, 255))
        windowSurface.blit(self.image1, self.rect_1)


        if self.rect_2.right < 890:
            self.rect_2.left = self.rect_1.right
        else:
            self.rect_2.left -= 5

        windowSurface.blit(self.image2, self.rect_2)