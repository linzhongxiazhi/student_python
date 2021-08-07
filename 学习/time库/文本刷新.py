#文本刷新
import time
print("-----程序开始-----")
num1=10
for i in range(num1+1):
    a="**"*i
    b="--"*(num1-i)
    c=(i/num1)*100
    print("{:^3.0f}%[{}->{}]".format(c,a,b))
    time.sleep(0.1)

print("-----程序结束-----")
