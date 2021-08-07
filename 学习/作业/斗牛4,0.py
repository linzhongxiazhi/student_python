# 斗牛4,0
 #  去除组合元素相同的元素
def func(n):
    ls1 = []
    ls2 = []
    for i in n:
        for x in str(i):
            ls1.append(x)
            ls1.sort()
            ls2.append(ls1)
    print(ls2)

func([123,321])
