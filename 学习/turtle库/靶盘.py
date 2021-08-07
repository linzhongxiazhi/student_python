#靶盘
from turtle import *
setup(900,900,0,0)
pencolor("green")
pensize(300)
goto(-350,350)
fd(700)

for i in range(2):
    circle(-100,180)
    fd(700)
    circle(100,180)
    fd(700)
goto(0,0)
pensize(15)
pencolor("red")
circle(5)

pensize(12)

yanse=['white','black']
r=10

for i in range(100):
    pencolor(yanse[i%len(yanse)])
    circle(r)
    r=r+10
    penup()
    goto(0,-10*(i+1))
    pendown()

done()