#回文数判断
num1=input("输入一串数字:")
num2=num1[::-1]
if num1==num2:
    print(num1+"是回文数")
else:
    print(num1+"不是回文数")
