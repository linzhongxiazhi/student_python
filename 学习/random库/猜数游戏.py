num1= int(1)
num2= int(input("输入一个0-9的整数:"))
num3=0
if 0<=num2<=9:
    while True:

        num3=num3+1
        if num2==num1:
            print("第{}次,猜中了".format(num3))
            break
        else:
            if num2<num1:
                print("很遗憾,猜小了")
                break
            if num2>num1:
                print("很遗憾,猜大了")
                break

else:
    print("你输入的数不在范围内呢")
