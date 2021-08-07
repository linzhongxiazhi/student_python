# 计数法比较异序词
def jsfun(s1,s2):
    """计数法比较异序词"""

    alist = [0] * 26
    blist = [0] * 26

    for i in s1:
        pos = ord(s1[i] - ord("a"))
        alist[pos] += 1

    for i in s2:
        pos = ord(s2[i] - ord("a"))
        blist[pos] += 1
    print(alist,"\n",blist)





jsfun("abc","cba")