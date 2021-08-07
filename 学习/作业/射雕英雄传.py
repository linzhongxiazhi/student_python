#射调英雄转文本分析
import jieba
r = open("射雕英雄传-网络版.txt","r",encoding="utf-8")
print(r)
txt = r.read()
b = jieba.lcut(txt)
ds = {}
for i in b:
    if len(b) == 1:
        continue
    elif i in[", ","。","“"]:
        continue
    else:
        ds[i] = ds.get(i,0)+1
del ds['\n']
ls = list(ds.items())
ls.sort(key=lambda x:x[1],reverse=True)
print(ls)

for i in ds:
    ls.append("{},")
