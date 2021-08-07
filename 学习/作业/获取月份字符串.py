#如何实现获取月份字符串，根据1-12的数字返回月份名称
yf="一月二月三月四月五月六月七月八月九月十月十一月十二月"
num1=eval(input("输入数字:"))
num2 = 0
if num1 in range(1,10):
    num2=(num1-1)*2
    print("输出:",yf[num2,num2+2])
elif num1 in[11]:
    print("十一月")
elif num1 in[12]:
    print("十二月")
else:
    print("输入有误")


