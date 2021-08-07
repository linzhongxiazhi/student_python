# 高斯求和
import time

num1 = eval(input("输入要求和的总数:"))
t1 = time.perf_counter()
num2 = ((num1+1)*num1)/2
print("从1到{}的和为:{}".format(num1, num2))
t2 = time.perf_counter()
t3 = t2-t1
print("程序运行时间为:{}s".format(t3))