import pygame
import sys
from interface.Background import Background
from interface.Dinosaur import Dinosaur
from interface.Score import ScoreInterface

# 全局初始化
pygame.init()
# 音效初始化
pygame.mixer.init()
# 设置窗口大小
resolution = width, height = 900, 300
# 设置全局分辨率
windowSurface = pygame.display.set_mode(resolution)
# 设置标题
pygame.display.set_caption("Dino")
# 设置图标
icon = pygame.image.load("./material/picture/icon.png")
pygame.display.set_icon(icon)
# 加载背景图
bgSurface = pygame.image.load("./material/picture/background.png")
# 加载恐龙图
image_list = []
for i in range(1, 7):
    image = pygame.image.load(f"./material/picture/Dino{i}.png")
    image_list.append(image)

# 背景音乐
pygame.mixer.music.load("./material/sound/背景音效2.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

# 加载音效
jumpSound = pygame.mixer.Sound("./material/sound/跳跃音效.mp3")

# 加载字体
textFont = pygame.font.Font("./material/MaoKenWangXingYuan-2.ttf",15)

# 初始化分数
score = 0
# 初始化时间
time = 1000

# 创建时钟对象
clock = pygame.time.Clock()

# 创建背景对象
background = Background(bgSurface)
# 创建恐龙对象
dinosaur = Dinosaur(image_list)
# 创建字体对象
scoreInterface = ScoreInterface(textFont)

if __name__ == "__main__":
    
    # 开启消息循环
    while True:
        # 事件处理
        for event in pygame.event.get():
            # 处理退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 处理键盘事件 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE and dinosaur.rect.y == 240:
                    # 绘制恐龙
                    dinosaur.UP()
                    # 发出音效
                    jumpSound.play()

        # 绘制背景
        background.draw(windowSurface)

        # 绘制恐龙
        dinosaur.draw(windowSurface)

        # 绘制分数
        # 获取时间
        t = pygame.time.get_ticks() 
        if t > time:
            score += 1
            time += 1000
        scoreInterface.draw(windowSurface,f"Score: {score}")

        # 刷新界面
        pygame.display.flip()

        # 时钟停留1帧
        clock.tick(60)
