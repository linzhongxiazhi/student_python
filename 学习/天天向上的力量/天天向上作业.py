#天天向上
num1=1
num2=1
for i in range(365):
    if i%7 in [1,2,3]:
        num1=num1*(i+num2)
    elif i%7 in [4,5,6,0]:
        num1=num1*(num2+
print(num1)
