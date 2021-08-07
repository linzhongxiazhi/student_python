# 随机生成一个QQ号
from random import *
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
list2 = []
for i in range(9):
    a = randint(0,len(list1)-1)
    list2.append(a)
print(len(list2))
for i in list2:
    print(i,end="")

