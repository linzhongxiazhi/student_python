# 随机生成n位数的和 平均数 方差 与中位数
from random import *
from time import *
from math import *

# 生成一个随机列表
t = perf_counter()
list1 = []
for i in range(10):
    num1 = randint(0, 100)
    list1.append(num1)
list1.sort()
print("随机生成的数为:", list1)
# 求和
num2 = 0  # 和
for i in list1:
    num2 += i
print("和为:", num2)
# 平均数
len1 = int(len(list1))
num3 = num2 / len1
print("平均数为:", num3)
# 方差
num4 = 0  # 方差
for i in list1:
    num4 += (i - num3) ** 2
num41 = num4 / len1
print("方差为:", num41)  # 方差
# 中位数
num5 = 0  # 中位数
len2 = float(len1 / 2)
len21 = 0
len22 = 0
if len1 % 2 == 0:
    len2 = int(len1 / 2)
    len21 = int(len2 + 1)
    num5 = (int(list1[len2]) + int(list1[len21])) / 2
    print("中位数为:", num5)
else:
    len22 = int(ceil(len2))-1
    print("中位数为:", list1[len22])
print("程序运行结束,运行时间为:{}s".format(perf_counter()))
