import pygame

times = 0
# 恐龙类
class Dinosaur():
    def __init__(self,image_list):
        self.image_list = image_list
        self.rect = self.image_list[0].get_rect()
        self.rect.x = 60
        self.rect.y = 240
    
    def draw(self,windowSurface):
        global times
        if times == 3:
            times = 0
        windowSurface.blit(self.image_list[times],self.rect)
        times += 1