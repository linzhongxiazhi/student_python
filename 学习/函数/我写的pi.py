# 蒙特卡罗方法求pi
# 假设在一个单位面积的正方形里有num1个点,每次随机生成一个坐标,判断坐标是否在圆内
# 如果在园内则 圆的面积+1
# pi的面积则为 pi=4 *(圆的面积/整体面积)
from random import *  # 调用 随机数库
from time import perf_counter  # 调用时间库 计时器
num1 = 1000 * 1000  # 定义一共有num1个点
num2 = 0  # 定义一个空变量 即园内点数(面积)
num4 = perf_counter()  # 定义变量给计时器
for i in range(1, num1 + 1):  # 循环 num1+1次
    x, y = random(), random()  # 随机生成两个随机数 即坐标
    num3 = x ** 2 + y ** 2  # 表达式
    if num3 <= 1:  # 判断随机生成的坐标是否在圆内
        num2 = num2 + 1  # 圆的面积＋1
pi = 4 * (num2 / num1)  # pi值
print("pi值为:{}".format(pi))  # 打印pi
print("所用时间:{:.5f}".format(perf_counter()))  # 打印计算所用时间
