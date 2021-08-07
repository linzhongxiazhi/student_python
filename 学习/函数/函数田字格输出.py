a="+"
b="-"
c="|"
d=" "
def fun1(n):
    for i in range(1,6*n+1):
        if i in [1,6]:
            print("{}{}{}".format(a,b*4,a))
        else:
            print("{}{}{}".format(c,4*d,c))
n=eval(input("输入:"))
fun1(n)

