#求和
num1=eval(input("输入:"))
num2,num3,i=0,0,0
while i<=num1:
    if i%2==0:
        num2+=i
    else:
        num3+=i
    i+=1
print("偶数:{}\n奇数{}".format(num2,num3))