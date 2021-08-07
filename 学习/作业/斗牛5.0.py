a = [3,3,4,3,7]
a_ = a[:]
b = a[:]
sum_5 = 0
for i in a:
    sum_5 += i
for i in a:
    a_.remove(i)
    for j in a_:
        quyu = (sum_5 - (i + j)) % 10
        if quyu == 0:
            print(b)
            b.remove(i)
            b.remove(j)
            print(str(b[0])+"+"+str(b[1])+"+"+str(b[2])+"="+str(b[0]+b[1]+b[2]))
            print(str(i)+"+"+str(j)+"="+str(i+j))
            b = a[:]