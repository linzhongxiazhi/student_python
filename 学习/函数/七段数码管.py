# 七段数码管
from turtle import *
from datetime import *


def fun(a):
    up()
    fd(5)
    down() if a in [0] else up()
    fd(40)
    up()
    fd(5)
    right(90)


def fun1(b):
    fun(0) if b in [2, 3, 4, 5, 6, 8, 9] else fun(1)
    fun(0) if b in [1, 3, 4, 5, 6, 7, 8, 9, 0] else fun(1)
    fun(0) if b in [2, 3, 5, 6, 8, 0] else fun(1)
    fun(0) if b in [2, 6, 8, 0] else fun(1)
    left(90)
    fun(0) if b in [4, 5, 6, 8, 9, 0] else fun(1)
    fun(0) if b in [2, 3, 5, 7, 8, 9, 0] else fun(1)
    fun(0) if b in [1, 2, 3, 4, 7, 8, 9, 0] else fun(1)
    up()
    seth(0)
    fd(10)
    down()


def fun2(c):
    for i in c:
        if i == "q":
            write('年', font=("Arial", 18, "normal"))
            up()
            fd(40)
        elif i == "w":
            write("月", font=("Arial", 18, "normal"))
            up()
            fd(40)
        elif i == "e":
            write("日", font=("Arial", 18, "normal"))
            up()
            fd(40)
        elif i == "r":
            write("时", font=("Arial", 18, "normal"))
            up()
            fd(40)
        elif i == "t":
            write("分", font=("Arial", 18, "normal"))
            up()
            fd(40)
        elif i == "y":
            write("秒", font=("Arial", 18, "normal"))
            up()
            fd(40)
        else:
            fun1(eval(i))


def fun3():
    speed(10000)
    up()
    fd(-500)
    down()
    pensize(5)
    color("red")
    fun2(datetime.now().strftime("%Yq%mw%de%Hr%Mt%Sy"))
    hideturtle()
    done()


fun3()
