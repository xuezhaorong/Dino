import pygame


# 背景类
class Background():
    def __init__(self, bgSurface , bgcloud):
        # 图片加载

        self.cloud1 = bgcloud
        self.cloud2 = bgcloud
        self.image1 = bgSurface
        self.image2 = bgSurface
        # 设置位置
        self.rect_1 = self.image1.get_rect()
        self.rect_1.left
        self.rect_1.bottom = 300

        self.rect_2 = self.image2.get_rect()
        self.rect_2.left
        self.rect_2.bottom = 300

        self.rect_3 = self.cloud1.get_rect()
        self.rect_3.left = 450
        self.rect_3.bottom = 160

        self.rect_4 = self.cloud2.get_rect()
        self.rect_4.left = 100
        self.rect_4.bottom = 190


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

        if self.rect_3.right < 0:
            self.rect_3.left = 905
        else:
            self.rect_3.left -= 2

        windowSurface.blit(self.cloud1, self.rect_3)

        if self.rect_4.right < 0:
            self.rect_4.left = 905
        else:
            self.rect_4.left -= 3

        windowSurface.blit(self.cloud2, self.rect_4)