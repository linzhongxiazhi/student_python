#4个数能组成多少种可能通
def func(a):
    ls=[]
    for i in range(1,5):
        for j in range(1,5):
            for k in range(1, 5):
                for n in range(1, 5):
                    b="{}{}{}{}".format(i,j,k,n)
                    ls.append(b)
    return ls
a=func(4)
print(len(a))