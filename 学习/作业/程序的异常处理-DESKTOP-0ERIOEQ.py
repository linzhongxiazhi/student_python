#程序的异常处理
try:
    num1="qwertyuiopasdfghjklzxcvbnm"
    num2=eval(input("输入一个数字:"))
    print(num1[num2])
except NameError:
    print("您的输入有误,请重新输入")
except IndexError:
    print("输入超出")
else:
    print("没有发生异常")
finally:
    print("程序运行完毕,不知是否发生异常.")