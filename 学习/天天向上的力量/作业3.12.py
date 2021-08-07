dayup=1
n=input("输入增加水平:")
for i in range(365):
    if i%7in[1,2,3,4,5,6]:
        dayup=dayup*(1+eval(n))
    else:
        dayup+=0
print("输出：{}".format(dayup))
        
