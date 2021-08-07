#求和叠加法
num1 = 10000000
num2 = 0
import time
for i in range(1,num1+1):
    num2+=i
print(num2)
print("{}s".format(time.perf_counter()))