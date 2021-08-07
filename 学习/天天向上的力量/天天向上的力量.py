#天天向上的力量 3停四进
num1=1
num2=0.01
for i in range(365):
    if i%10 in[0]:
        num1=num1
    elif i%7 in[1,2,3,4,5,6,7,8,9]:
        num1=num1+num1*num2
print("{:.2f}".format(num1))