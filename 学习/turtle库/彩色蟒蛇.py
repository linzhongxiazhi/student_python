# 彩色蟒蛇
from distutils.core import setup
from turtle import * 
setup(900,900,0,0)  # 彩色蟒蛇

penup()
speed(1000)
fd(-250)
pendown()
pensize(25)
a=['red','blue','green','cyan']
seth(-40)
for i in range (4):
    color(a[i])
    circle(40,80)
    circle(-40,80)
color("purple")
circle(40,80/2)
fd(40)
circle(16,180)
fd(40*2/3)
done()
