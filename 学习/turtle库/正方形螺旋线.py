#2.8
from turtle import *
speed(10)
setup(900,900,0,0)
pensize(1)
pencolor("red")
a=1
for i in range (10000):
    seth(90)
    fd(a)
    seth(180)
    fd(a+2)
    seth(270)
    fd(a+4)
    seth(0)
    fd(a+6)
    a=a+8
done()

