#斐波那契数列递归
def fun(n):
    if n ==1:
        return 1
    elif n ==2:
        return 1
    else:
        return fun(n-1)+fun(n-2)
b=eval(input("输入多少个月："))
a=fun(b)
print("总共有{}对小兔崽子诞生".format(a))


