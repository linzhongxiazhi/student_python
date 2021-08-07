#整数求和2,0
n=['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15']
n2=int(input("输入一个小于29的整数:"))
n3=len(n)
i,x=0,1
for i in range(int(n3)):
    for x in range(int(n3-1)):
        if int(n[i])+int(n[x]) == n2:
            print("{}+{}={}".format(n[i],n[x],n2))
else:
    print("超出")
