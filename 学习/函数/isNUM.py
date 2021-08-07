#　isnum函数,如果输入的字符串可以表现为整数,浮点数或复数形式则可返回True,否则返回False
def isNum(str):
    n = type(eval(str))
    if n == type(1):
        return print(True)
    elif n == type(1.0):
        return print(True)
    elif n == type(1+1j):
        return print(True)
    else:
        return print(False)

isNum(input("请输入:"))
