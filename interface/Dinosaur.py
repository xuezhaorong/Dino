import pygame

times = 0

# 恐龙类
class Dinosaur():
    def __init__(self,image_list):
        self.image_list = image_list
        self.rect = self.image_list[0].get_rect()
        self.rect.x = 60
        self.rect.y = 240
        self.speed = 0
        # 下降标志
        self.flag = False

    def draw(self,windowSurface):
        global times
        
        # 下降
        if self.flag:
            self.rect.y += self.speed
            if self.speed != 20:
                self.speed += 2
            else:
                self.flag = False
                self.speed = 0
        else:
            self.rect.y -= self.speed
            if self.speed > 0:
                self.speed -= 2
            if self.speed == 0 and self.rect.y != 240 and self.flag == False:
                # 开始下降
                self.flag = True

        if times == 16:
            times = 0
        windowSurface.blit(self.image_list[times],self.rect)
        times += 1


    def UP(self):
        self.speed = 20 