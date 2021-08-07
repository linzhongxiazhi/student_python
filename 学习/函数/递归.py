#递归
n=eval(input("输入一个数字："))
if n==0 :
    print(1)
else:
    for i in range(1,n):
        n*=i
print(n)
