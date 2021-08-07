a = input("请输入二进制：")
b = len(a)
ls = []
for i in range(b):
    if a[i] not in ["1", "0"]:
        print("您输入的不是二进制数字")
        break
else:
    for i in range(b):
        c = eval(a[i]) * 2 ** (b - 1 - i)
        ls.append(c)
    d = 0
    for i in ls:
        d += i
    print("{}转化为二进制为：{}".format(a, d))
