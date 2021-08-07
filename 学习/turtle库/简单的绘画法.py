ls1 = [1,10,20,30,40,50,60,70,80]
ls2 = ["red","green","white","black","grey","violet","purple","blue","gold"]
ls3 = [20,40,60,80,100,120,140,160,180]
import turtle
for i in range(len(ls1)):
    turtle.pensize(ls1[i])
    turtle.pencolor(ls2[i])
    turtle.circle(ls3[i])
    turtle.up()
    turtle.goto(0,-ls3[i])
    turtle.down()
turtle.hideturtle()
turtle.done()