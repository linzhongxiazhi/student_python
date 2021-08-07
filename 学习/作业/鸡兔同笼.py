# 鸡兔同笼
from sympy import *
num1 = int(input("请输入有多少个头:"))
num2 = int(input("请输入有多少只脚:"))
x = Symbol("x")  # 设鸡为x
y = Symbol('y')  # 设兔为y
print(solve([x + y - num1, 2*x +4*y - num2], [x, y]))  # 解方程

