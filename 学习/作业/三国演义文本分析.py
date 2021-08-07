# 三国演义文本分析
import jieba
ls1 =["c"]
txt = open("三国演义.txt","r",encoding="utf-8").read()
word = jieba.lcut(txt)
dt = {}
for i in word:
    if len(i) == 1:
        continue
    else:
        dt[i] = dt.get(i,0)+1
ls = list(dt.items())
ls.sort(key=lambda x:x[1],reverse=True)
for i in range(15):
    x,y = ls[i]
    print("{:<10}{:>10}".format(x,y))