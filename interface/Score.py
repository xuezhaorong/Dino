import pygame
# 分数类
class ScoreInterface():
    def __init__(self,textFont):
        self.textFont = textFont
    
    def draw(self,windowSurface,score):
        textSurface = self.textFont.render(score,True,(64,64,64))
        windowSurface.blit(textSurface,(10,10))
