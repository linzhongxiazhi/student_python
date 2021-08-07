# 哈姆雷特词频统计
def fun1():
    t = open("D://桌面/哈姆雷特.txt","r").read()
    t = t.lower()
    for i in '!"#$%&()*+_,-./:;<=>?@[\\]^_{|}':
        t.replace(i," ")
    return t


txt = fun1()
zidian = {}
words =txt.split()
for i in words:
    if i in zidian:
        zidian[i]=zidian[i]+1
    else:
        zidian[i]=1
list1= list(zidian.items())
list1.sort(key=lambda x:txt[1],reverse=True)
for i in range(10):
    word,count =list1[i]
    print("{:<10}{:>5}".format(word,count))