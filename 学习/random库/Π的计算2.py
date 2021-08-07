#Π的计算
n=100
pai=0
for k in range(n):
   pai+=1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print("输出：{}".format(pai))