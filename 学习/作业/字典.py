x=[56.78,95,93]
print("参加考试的人数是",len(x),"人")
print("这些分数分别是:")
print(x)
for i in range(len(x)):
    print(x[i])
x[0]=60
print(x)
y=eval(input("请输入新的分数:"))
x.append(y)
print(x)