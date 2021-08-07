# 基本统计值计算
from math import sqrt
def fun1():   # 将用户输入的所有数转化为列表
    str1 = input("\r请输入数字(什么都不输入结束输入):",)
    list1 = []
    while str1 != "":
        list1.append(eval(str1))
        str1 = input("\r请输入数字(什么都不输入结束输入):",)
    return list1

def fun2(list2):  #平均数
    num1 = 0.0
    for i in list2:
        num1 += i
    return num1/len(list2)

def fun3(list2,list3): #方差
    num2 = 0.0
    for i in list2:
        num2 += (i - list3)**2
    return sqrt(num2/(len(list2)-1))

def fun4(list2):  # 中位数
    list3 = sorted(list2)
    a = len(list2)
    if a % 2 == 0:
        b = (list3[a//2-1]+list3[a//2])/2
    else:
        b = list3[a//2]
    return b
def max1(list2):
    list2 = list(set(list2))
    a = max(list2)
    return a
def min1(list2):
    list2 = list(set(list2))
    a = min(list2)
    return a
n = fun1()  #主体函数
x = fun2(n) #平均数
print("平均数为:{}\n方差为:{}\n中位数为:{}\n最大值为{}\n最小值{}".format(x,fun3(n,x),fun4(n),max1(n),min1(n)))

