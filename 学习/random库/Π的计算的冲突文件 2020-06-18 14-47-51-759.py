pi=0
for k in range(100000):
    pi+=1/pow(16,k)*(4/(8*k+1)-2/(8*k+4)-1/(8*k+5)-1/(8*k+6))
print("{:.100f}".format(pi))