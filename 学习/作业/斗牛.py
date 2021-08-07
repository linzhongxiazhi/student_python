# 斗牛
ls = input("请输入5个数由','分隔:")
ls=ls.split(",")
print(ls)
a=0
for i in ls:
    a += int(i)

for i in ls:
    for x in ls:
        if x == i:
            continue
        else:
            for y in ls:
                if y ==i and y==x:
                    continue
                else:
                    if (int(i) +int(x)+int(y))%10 == 0:
                        print("{}+{}+{}={}".format(i,x,y,int(i) +int(x)+int(y)),end='   ')
                        b = a -(int(i) +int(x)+int(y))
                        print(b)
                    else:
                        ls.sort()
                        print(ls)
