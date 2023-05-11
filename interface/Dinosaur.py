import pygame

times = 0

# 恐龙类
class Dinosaur(pygame.sprite.Sprite):
    def __init__(self,image_list,down_list):
        super().__init__()
        self.image_list = image_list
        self.rect = self.image_list[0].get_rect()
        self.rect.x = 60
        self.rect.y = 245
        self.speed = 0
        # 下降标志
        self.flag = False
        # 下蹲图
        self.down_list = down_list
        self.d_rect = self.down_list[0].get_rect()
        self.d_rect.x = self.rect.x
        self.d_rect.y = self.rect.y + 20
        # 下蹲标志
        self.down_f = False
        # 创建遮罩
        self.mask = pygame.mask.from_surface(self.image_list[0])

    def draw(self,windowSurface):
        global times
        
        # 下降
        if self.flag:
            self.rect.y += self.speed
            if self.speed != 24:
                self.speed += 2
            else:
                self.flag = False
                self.speed = 0
        else:
            self.rect.y -= self.speed
            if self.speed > 0:
                self.speed -= 2
            if self.speed == 0 and self.rect.y != 245 and self.flag == False:
                # 开始下降
                self.flag = True

        if times == 16:
            times = 0
        
        image = self.down_list[times]
        if self.down_f:
            image = self.down_list[times]
            windowSurface.blit(image,self.d_rect)
        else:  
            image = self.image_list[times]
            windowSurface.blit(image,self.rect)

        # 更新遮罩
        self.mask = pygame.mask.from_surface(image)
        
        times += 1


    def UP(self):
        self.speed = 24 
    
    # 画下蹲图
    def Down(self):
        self.down_f = not self.down_f