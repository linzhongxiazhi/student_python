# 三国演义分词
import jieba
t = open("三国演义.txt","r",encoding="UTF-8").read()
tx=jieba.lcut(t)
zidian = {}
for i in tx:
    if len(i) == 1:
        continue
    else:
        zidian[i] = zidian.get(i,0) +1
list1 = list(zidian.items())
list1.sort(key=lambda x:x[1],reverse =True)
for i in range(15):
    x,y=zidian[i]
    print("{:<10}{:>5}".format(x,y))
print("你算吊毛?")