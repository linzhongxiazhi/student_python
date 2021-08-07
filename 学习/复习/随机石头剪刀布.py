# 调用随机数库
import random


# 1代表石头 2代表剪刀 3代表布
# 定义一个函数把石头转换为1 剪刀转化为2 布转换为3 反过来也一样
def fun(a):
    if a == "石头":
        a = 1
        return a
    elif a == "剪刀":
        a = 2
        return a
    elif a == "布":
        a = 3
        return a
    elif a == 1:
        a = "石头"
        return a
    elif a == 2:
        a = "剪刀"
        return a
    elif a == 3:
        a = "布"
        return a


# 玩家输入
x = input("请输入:")
print("玩家出的是:{}".format(x))
a = fun(x)

# 电脑输入
b = random.randint(1, 3)
print("电脑出的是:{}".format(fun(b)))

# 胜利规则
# 1胜2
# 2胜3
# 3胜1
if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print("真棒,你赢了!")

# 相同平局
elif a == b:
    print("平局")

# 不同则玩家输
else:
    print("你输了")
