#带刷新的文本进度条
import time
num1=100
print('程序开始'.center(num1,'-'))
t=time.perf_counter()
for i in range(num1+1):
    a='*'*i
    b='-'*(num1-i)
    c=(i/num1)*100
    t=time.perf_counter()
    print("\r{:3.0f}% [{}->{}] {:3f}s".format(c,a,b,t),end = "")
    time.sleep(0.01)
print('\n'+''"程序结束".center(num1,"-"))

