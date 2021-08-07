#笑傲江湖
r = open("笑傲江湖.txt","r",encoding='utf-8')
b =open("笑傲江湖-字符统计.txt","w",encoding="utf-8")
txt = r.read()
dt ={}
for i in txt:
    dt[i]= dt.get(i,0)+1
del dt[' ']
del dt['\n']
ls = []
for i in dt:
    ls.append("{}:{}".format(i,dt[i]))
b.writelines(ls)
r.close()
b.close()
