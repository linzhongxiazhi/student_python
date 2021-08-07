# 统计字符串
str1=str(input("输入一串字符串:"))     # 获得用户输入的字符串
list1 = []
num1 = -1
set1 = set()

for i in str1:
    a = ord(i)
    list1.append(a)
print(list1)
for i in list1:
    b = list1.count(i)
    c = "字符{}出现的次数为{}".format(chr(i),b)
    set1.add(c)
    list(set1)
for i in set1:
    print(i)

