#汇率转化
a=eval(input("输入数值："))
b=input("输入符号(R代表人民币，M代表美元)：")
if b in ['m','M']:
    r=6*a
    print("输出：{:.2f}人民币".format(r))
elif b in ['r','R']:
    m=a/6
    print("输出：{:.2f}美元".format(m))
else:
    print("输入有误")