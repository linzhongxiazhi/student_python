#重复元素判定
def fun1(X):
    a=len(X)
    y=set(x)
    b=len(y)
    if b<a:
        return 1
    else:
        return 2
n=[1,2,3,4,5,6,7,8,9]
fun1(n)
