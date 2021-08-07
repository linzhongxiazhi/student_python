#圆的面积和周长
import math
num1=eval(input("输入半径："))
s=math.pi*pow(num1,2)
c=math.pi*num1*2
print("圆的周长为:{:.2f}\n圆的面积为:{:.2f}".format(c,s))