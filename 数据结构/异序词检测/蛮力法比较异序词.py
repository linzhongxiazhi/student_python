#蛮力法
def mlfun(s1,s2):
    """判断两个字符串是否为异序词

    s1:字符串1

    s2:字符串2"""

    def zh(l):
        """输出字符串的所有排列方式"""
        if len(l) <= 1:
            return l
        cl = []
        for i in range(len(l)):
            for j in zh(l[0:i] + l[i + 1:]):
                cl.append(l[i] + j)

        cl = list(set(cl))
        return cl

    #输出字符串1所有的排列顺序
    alist = zh(s1)

    #判断字符串2是否在字符串所有的排列顺序里
    #如果是,返回True , 否则返回 False
    if s2 in alist:
        return True
    else:
        return False

a = mlfun("12355","32145")
print(a)




