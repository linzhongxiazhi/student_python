from random import *
try:
    num1=int(randint(0,100))
    num2=0
    while True:
        num2+=1
        num3=int(input("输入一个0-100的数:"))
        if 0<=num3<=100:
            if num3 ==num1:
                print("真厉害,第{}次就猜中了呢".format(num2))
                break


            elif num3<num1:
                print("真遗憾,猜小了呢,再来一次吧!")
                continue
            elif num3>num1:
                print("真遗憾,猜大了呢,再猜一次吧!")
                continue
        else:
            print("您输入的数不在范围内呢")
except ValueError:
    print("输入内容必须为整数!")
except:
    print("其他错误")
else:
    print("没有出错")
finally:
    print("程序运行完毕,不知道有没有错")


