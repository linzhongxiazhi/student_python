def user_Input():  # 获得用户输入,并将用户输入的字符串转化为整形,并按升序排列
    a = input("请用户输入5个数字并用','分隔:")
    a = a.split(",")
    b = []
    for i in a:
        b.append(int(i))
    b.sort()
    return b

def judge(n):  # 判断5个数哪3个数加起来是10的倍数,返回一个字典类型
    se =set()
    se1=set()
    x =[]
    for x1 in n:
        for x2 in n:
            for x3 in n:
                x.append(x1);x.append(x2);x.append(x3)
                x.sort()
                for i in x:
                    if n.count(i) == x.count(i):
                        if sum(x) %10 == 0:
                            print(x)
                            se.add("{}+{}+{}={}   剩下的和为{}".format(x[0],x[1],x[2],sum(x),sum(n)-sum(x)))
                            x.clear()
                    else:
                        pass
                else:
                    x.clear()
    return se
ls=user_Input(); se =judge(ls)
if se:
    for i in se:
        print(i)
else:
    print("没有10的倍数,升序排列为{}".format(ls))
