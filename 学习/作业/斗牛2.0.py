# 斗牛2.0
def user_Input():   # 获得用户输入,并将用户输入的字符串转化为整形,并按升序排列
    a =input("请用户输入5个数字并用','分隔:")
    a = a.split(",")
    b = []
    for i in a:
        b.append(int(i))
    b.sort()
    return b


def judge(n):  # 判断5个数哪3个数加起来是10的倍数
    b = 0
    ls = []
    for i in n:
        b += i
    for x1 in n:
        for x2 in n:
            for x3 in n:
                if x1 != x2 and x1 != x2 and x2 != x3:
                    if (x1+x2+x3)%10 == 0:
                        a = x1 +x2 +x3

                        c = b-a
                        print("{}+{}+{}={}".format(x1,x2,x3,a),end='   ')
                        print("剩下的数字和为{}".format(c))
judge(user_Input())