import pygame
import sys
from interface.Background import Background
from interface.Dinosaur import Dinosaur
from interface.Score import ScoreInterface
from interface.Restart import RestartInterface
from interface.Barrier import BarrierInterface
from interface.Barrierbird import BarrierbirdInterface
import random
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
# 加载背景云朵图
bgcloud = pygame.image.load("./material/picture/cloud.png")
# 加载恐龙图
image_list = []
for i in range(1, 17):
    image = pygame.image.load(
        f"./material/picture/Dino{i}.png").convert_alpha()
    image_list.append(image)
# 加载恐龙下蹲图
down_list = []
for i in range(1, 17):
    down_image = pygame.image.load(
        f"./material/picture/down{i}.png").convert_alpha()
    down_list.append(down_image)
# 加载失败图
failImage = pygame.image.load("./material/picture/gameover.png")
# 加载重启按钮图
restartImage = pygame.image.load("./material/picture/Restart.png")
# 加载障碍图
barrier_list = []
for i in range(1, 7):
    barrier_image = pygame.image.load(
        f"./material/picture/Barrier{i}.png").convert_alpha()
    barrier_list.append(barrier_image)
barrierbird_list = []
for i in range(1,29):
    barrierbird_image = pygame.image.load(
        f"./material/picture/Bird{i}.png").convert_alpha()
    barrierbird_list.append(barrierbird_image)
# 创建障碍Group
seGroup1 = pygame.sprite.Group()
seGroup2 = pygame.sprite.Group()
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
background = Background(bgSurface, bgcloud)
# 创建恐龙对象
dinosaur = Dinosaur(image_list, down_list)
# 创建字体对象
scoreInterface = ScoreInterface(textFont)
# 创建重启按钮对象
restartInterface = RestartInterface(restartImage)

# 分数列表
score_list = []

# 失败标志
fail = False
# 重开函数


def restart():
    global score, time, seGroup1, score_list
    score = 0
    time = currentTime
    # 开始音乐播放
    pygame.mixer.music.unpause()
    # 清空seGroup
    for se in seGroup1:
        seGroup1.remove(se)
    for se in seGroup2:
            seGroup2.remove(se)
    # 清空socre_list
    score_list.clear()


def cleanSprit():
    global seGroup1, score_list
    for se in seGroup1:
        if se.rect.x < 0:
            score_list.append(se.score)
            seGroup1.remove(se)
    global seGroup2
    for se in seGroup2:
        if se.rect.x < 0:
            score_list.append(se.score)
            seGroup2.remove(se)



# 创建障碍


def createBarrier():
    global seGroup1, barrier_list
    n = random.randint(0, 5)
    barrier1 = BarrierInterface(barrier_list[n], n+1)
    seGroup1.add(barrier1)
def createBarrierBird():
    global seGroup2, image_list
    barrier2 = BarrierbirdInterface(barrierbird_list,2)
    seGroup2.add(barrier2)
# 计算得分


def calScore():
    global score_list, score
    for i in score_list:
        score += i
    score_list.clear()


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
            elif event.type == pygame.KEYDOWN and not fail:
                # 下蹲事件
                if event.key == pygame.K_DOWN:
                    # 绘制恐龙
                    dinosaur.Down()
                    # 发出音效
                    # jumpSound.play()
                elif event.key == pygame.K_SPACE and dinosaur.rect.y == 245 and not dinosaur.down_f:
                    # 绘制恐龙
                    dinosaur.UP()
                    # 发出音效
                    jumpSound.play()
            # 按键松开
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    dinosaur.Down()
            # 处理鼠标事件
            elif event.type == pygame.MOUSEBUTTONDOWN and fail:
                if restartInterface.rect.collidepoint(event.pos):
                    fail = False
                    restart()
        if not fail:
            # 绘制背景
            background.draw(windowSurface)

            # 绘制恐龙
            dinosaur.draw(windowSurface)

            # 计算得分
            calScore()

            # 内部计时器
            t = pygame.time.get_ticks()
            if t > time:
                score += 1
                time += 1000
                if time % 1000 == 0:
                    createBarrier()
                    createBarrierBird()

            # 绘制得分
            scoreInterface.draw(windowSurface, f"Score: {score}")

            # 绘制障碍
            seGroup1.update()
            seGroup1.draw(windowSurface)
            seGroup2.update()
            for se in seGroup2:
                se.draw(windowSurface)



            # 碰撞检验
            if pygame.sprite.spritecollide(dinosaur, seGroup1, False, pygame.sprite.collide_mask):
                fail = True
                # 暂停音乐
                pygame.mixer.music.pause()
                # 触发音效
                failSound.play()
            if pygame.sprite.spritecollide(dinosaur, seGroup2, False, pygame.sprite.collide_mask):
                fail = True
                # 暂停音乐
                pygame.mixer.music.pause()
                # 触发音效
                failSound.play()

            # 清理内存
            cleanSprit()
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
