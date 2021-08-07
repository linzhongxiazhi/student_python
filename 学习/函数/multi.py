#定义multi函数,参数不限,返回所有参数的乘积
def multi(a,*b):
    for i in b:
        a *= i
    return a
a=multi(1,2,3)
print(a)