#PM2.5空气质量提醒
num1=input("输入空气质量：")
num1=eval(num1)
if num1>=75 :
    print("有污染")
elif 35<=num1<75:
    print("空气质量良好，建议适度室外运动")
elif num1<35:
    print("空气质量优，建议室外运动")
else:
    print("非法输入")

