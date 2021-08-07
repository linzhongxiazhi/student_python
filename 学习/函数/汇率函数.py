#定义函数
def fun(num1):

    if num1[-1] in ['m','M']:
        y=7.1503*eval(num1[0:-1])
        print("人民币为:{}".format(y))
    if num1[-1] in ['y','Y']:
        m=eval(num1[0:-1])/7.1503
        print("美元为:{}".format(m))
    else:
        print("非法输入"+"\n可能是没输入符号")
    return
a=input("输入(y代表人民币,m代表美元):")
fun(a)
