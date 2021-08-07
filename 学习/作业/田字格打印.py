#田字格打印
num1=eval(input("输入一个奇数:"))
a="+"
b="-"
c="|"
d=" "
num2=(num1-1)//2+1
num3=(num1-3)//2
if num1%2==0:
    print("您输入的不是奇数请重新输入")
else:
    for i in range(1,num1+1):
        if i in [1,num2,num1]:
            print("{} {} {} {} {}".format(a,b*num3,a,b*num3,a))
        else:
            print("{} {} {} {} {}".format(c,d*num3,c,d*num3,c))


