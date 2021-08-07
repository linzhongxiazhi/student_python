# 质数判断
def func(n):
    if n ==1:
        return print(True)
    elif n ==2:
        return print(True)
    else:
        for i in range(2,n+1):
            if n % i == 0:
                return print(False)

            else:
                return print(True)
n = eval(input())
func(n)