#异序词:组成元素一样,排列顺序不一样.
#清点法,比较a字符串中每个字符是否出现在字符串b中,
def func(s1,s2):
    s3 = list(s2)
    a = 0
    x =True
    while a<len(s1) and x:
        b=0
        y =True
        while b<len(s3) and not y:
            if s1[a] == s3[b]:
                y=True
            else:
                b += 1
        if y:
            s3[b] = None
        else:
            x = False

        a += 1
        return x
print(func("1923","322501"))