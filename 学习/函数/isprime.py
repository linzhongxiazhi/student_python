# 定义一个isprime函数, 如果是质数则返回True , 如果不是则返回False
def isprime(int):
    for i in range(1,int+1):
        if i ==1:
            continue
        elif i == int:
            continue
        else:
            if int % i == 0:
                return False
            else:
                return True
a = isprime(eval(input("请输入一个数")))
print(a)