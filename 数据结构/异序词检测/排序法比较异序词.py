#排序法比较异序词

def fun(s1,s2):
    # 转化为列表
    alist1 = list(s1)
    alist2 = list(s2)

    #对列表进行排序
    alist1.sort()
    alist2.sort()

    #定义下标计数器和返回值
    a = 0
    b = True

    #判断每个列表的序列元素和另一个对应列表是否相同
    while a<len(s1) and b:
        if len(alist1) != len(alist2):
            b =False
        elif alist1[a] == alist2[a]:
            a += 1
        else:
            b =False
    return b

a = fun("12234","32115")
print(a)