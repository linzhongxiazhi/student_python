#26个字母下一个单词是什么
import random
dc = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
while True:
    a = random.randint(0,24)
    b=dc[a]
    c =input("请打印{}后面是什么:".format(b))
    while True:
        if c == dc[a+1]:
            print("你猜对了.")
            break
        else:
            c = input("请打印{}后面是什么:".format(b))