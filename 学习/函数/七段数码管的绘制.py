#定义七段数码管
from turtle import *
from datetime import *
def fun(a):
    down() if a in [0] else up()
    fd(40)
    right(90)
def fun1(b):
    fun(0) if b in [2,3,4,5,6,7,8,9] else fun(1)
    fun(0) if b in [0,1,3,4,5,6,7,8,9] else fun(1)
    fun(0) if b in [0,2,3,5,6,8,9] else fun(1)
    fun(0) if b in [0,2,6,8] else fun(1)
    left(90)
    fun(0) if b in [0,4,5,6,8,9] else fun(1)
    fun(0) if b in [0,2,3,5,6,7,8,9] else fun(1)
    fun(0) if b in [0,1,2,3,4,7,8,9] else fun(1)
    seth(0)
    up()
    fd(30)
    down()
def fun2(c):
    for i in c :
        try:
            if i in ["-"]:
                continue
        except:
            continue
        fun1(eval(i))
def fun3():
    up()
    fd(-300)
    d=str(datetime.now())
    fun2(d)
fun3()





