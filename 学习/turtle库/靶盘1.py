#粗细不同的同心圆,笔的颜色不同
import turtle
#第一个圆
turtle.pensize(1)
turtle.pencolor("red")
turtle.circle(10)
turtle.up() #抬起画笔
turtle.goto(0,-10)
turtle.down()#放下画笔
#第二个圆
turtle.pensize(3)
turtle.pencolor("green")
turtle.circle(20)
turtle.up()
turtle.goto(0,-20)
turtle.down()
#第三个圆依次类推






#隐藏画笔和保留窗口不消失
turtle.hideturtle()
turtle.done()
