from random import *
while True:
    n=randint(1,100)
    if n%2==0:
        #print(n)
        continue
    if n%2==1:
        break
print(n)
#方法二
# from random import *
#a=randrange(1,100,2)
#print(a