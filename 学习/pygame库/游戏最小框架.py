# 游戏最小框架
# 1.导入库
import pygame, sys


# 2.初始化
pygame.init()
# 3.设定窗口 字体 背景颜色 游戏名称 等
gm = pygame.display.set_mode((400, 400))  # 窗口
#pygame.font("汉仪酷雅黑")  # 字体
pygame.display.set_caption("林钟的第一个游戏")  # 标题
# 4.保持游戏一直运行
# game loop 游戏循环
while True:
    # 5.检测事件
    for i in pygame.event.get():  # 检测事件
        if event.type == pygame.QUIT:  # 检测关闭按钮被点击的事件
            pygame.quit()
            sys.exit()  # 关闭






