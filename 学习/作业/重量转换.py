#重量转换
a=input("输入一个带符号数值：")
if a[-1] in ('g','G',): 
    kg=eval(a[0:-1])/1000
    print("输出:{}kg".format(kg))
elif a[-2]in('k','K'):
    g=eval(a[0:-2])*1000
    print("输出:{}g".format(g))
else:
    print("非法输入")