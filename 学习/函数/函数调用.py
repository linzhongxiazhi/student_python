
def fx():
    num1 = int(input("输入:"))
    y=1
    for i in range(1,num1+1):
        y=y*i
    print(y)
    return fx()
fx()