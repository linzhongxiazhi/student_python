# 重量计算
num1=eval(input("输入体重(kg):"))
for i in range(1,11):
    num2=num1+0.5*i
    num3=num2*0.165
    print("第{}年 地球:{:.2f}kg 月球:{:.3f}kg".format(i  , num2  , num3))