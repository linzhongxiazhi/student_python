dayup=1.0
n=input("输入增加量：")
for i in range(360):
    if i%30 in [1,2,3,4,5,6,7,8,9,10]:
        dayup=dayup*(1+eval(n))
    else:
        dayup=dayup+0
print("输出：{}".format(dayup))
    
