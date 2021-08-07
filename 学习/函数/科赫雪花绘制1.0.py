#科赫雪花绘制1.0
from turtle import *
c=eval(input("输入要绘制多少层:"))
def num1(a,b):
    if b == 0:
        fd(a)
    else:
        for i in [0,60,-120,60]:
            left(i)

            num1(a/3,b-1)
def fun1():
    up()
    goto(-300,50)
    speed(100000)
    down()
    color("red")
    num1(400,c)
    seth(240)
    num1(400,c)
    seth(120)
    num1(400,c)
    pensize(2)
    hideturtle()
    done()


fun1()

