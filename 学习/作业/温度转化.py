#2.1温度转换
a,b=eval(input("输入一个数值：")),input("输入符号：")
#b=input("输入符号：")
if b in ['f',"F"]:
    c=(a-32)/1.8
    print("转换后的温度为：{:.2f}C".format(c))
elif b in ['c','C']:
    f=1.8*a+32
    print("转化后的温度为：{:.2f}F".format(f))
else:
    print("输入有误")

#if a[-1] in ['F','f'] :
   # c=(a-32)/1.8
   # print("转换后的温度为:{}C".format(c))