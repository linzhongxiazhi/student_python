# 十进制转化为二进制
a = eval(input("输入十进制："))
i = 0
b = 0
ls = []
while True:
    b = a % 2
    a = a // 2
    ls.append(b)
    if a == 0:
        break
ls.reverse()
c = ""
for i in ls:
    c += str(i)
print(c)
