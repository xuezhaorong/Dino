import pygame
import sys
from interface.Background import Background
from interface.Dinosaur import Dinosaur
from interface.Score import ScoreInterface
from interface.Restart import RestartInterface

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
for i in range(1, 17):
    image = pygame.image.load(f"./material/picture/Dino{i}.png")
    image_list.append(image)
# 加载失败图
failImage = pygame.image.load("./material/picture/gameover.png")
# 加载重启按钮图
restartImage = pygame.image.load("./material/picture/Restart.png")

# 背景音乐
pygame.mixer.music.load("./material/sound/背景音效2.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(0.4)

# 加载音效
jumpSound = pygame.mixer.Sound("./material/sound/跳跃音效.mp3")
failSound = pygame.mixer.Sound("./material/sound/失败音效.mp3")

# 加载字体
textFont = pygame.font.Font("./material/MaoKenWangXingYuan-2.ttf", 15)

# 初始化分数
score = 0
# 初始化时间
currentTime = 1000
# 动态时间
time = 1000

# 创建时钟对象
clock = pygame.time.Clock()

# 创建背景对象
background = Background(bgSurface)
# 创建恐龙对象
dinosaur = Dinosaur(image_list)
# 创建字体对象
scoreInterface = ScoreInterface(textFont)
# 创建重启按钮对象
restartInterface = RestartInterface(restartImage)

# 失败标志
fail = False
# 重开函数


def restart():
    global score, time
    score = 0
    time = currentTime
    # 开始音乐播放
    pygame.mixer.music.unpause()


if __name__ == "__main__":

    RESET_TICK_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(RESET_TICK_EVENT, 0)

    # 开启消息循环
    while True:
        # 事件处理
        for event in pygame.event.get():
            # 处理退出事件
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # 处理键盘事件
            elif event.type == pygame.KEYDOWN and not fail:
                if event.key == pygame.K_SPACE and dinosaur.rect.y == 240:
                    # 绘制恐龙
                    dinosaur.UP()
                    # 发出音效
                    jumpSound.play()
                    # 处理鼠标事件
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if restartInterface.rect.collidepoint(event.pos):
                    fail = False
                    restart()
        if not fail:
            # 绘制背景
            background.draw(windowSurface)

            # 绘制恐龙
            dinosaur.draw(windowSurface)

            # 绘制分数
            t = pygame.time.get_ticks()
            if t > time:
                score += 1
                time += 1000
            scoreInterface.draw(windowSurface, f"Score: {score}")

        if time == 10000:
            fail = True

        # 计时器
        t = pygame.time.get_ticks()
        if t > currentTime:
            currentTime += 1000

        if fail:
            # 绘制失败图片
            windowSurface.blit(failImage, (260, 100))
            # 绘制重启按钮
            restartInterface.draw(windowSurface)

        # 刷新界面
        pygame.display.flip()

        # 时钟停留1帧
        clock.tick(60)
