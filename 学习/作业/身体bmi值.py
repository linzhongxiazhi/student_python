#身体bmi值
num1=eval(input("输入身高（米）："))
num2=eval(input("输入体重（千克）："))
bim=num2/pow(num1,2)
print("身体的BMI值为：{:.2f}".format(bim))
a=""#国外
b=""#国内
if bim<18.5:
    a="偏瘦"
    b="偏瘦"
elif 18.5<=bim<25:
    a="正常"
elif 18.5<=bim<24:
    b="正常"
elif 24<=bim<28:
    b="偏胖"
elif bim>=28:
    b="肥胖"
elif 25<=bim<30:
    a="偏胖"
else:
    a="肥胖"
print("国内：{}\n国外：{}".format(b,a))


