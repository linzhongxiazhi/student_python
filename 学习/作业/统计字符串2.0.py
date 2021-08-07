# 统计字符串2.0
str1 = list(input("随便输入:"))  # 将用户输入的字符串转化为列表
list1, list2, list3 = [], [], []  # 定义三个空列表
set1 = set()  # 定义一个空集合 用来去重

for i in str1:
    a = str1.count(i)  # 统计i出现的次数 例如1231中1出现了2次 1=2
    list1.append(i)  # 将i放入列表1中 一一对应
    list2.append(a)  # 将a放入列表2中 一一对应 
b = max(list2)      # 得到出现次数最多的元素的次数  例如7出现了8次 b=8
for i in range(len(list2)):  # 用来找到次数最多的元素的序号
    if list2[i] == b:
        list3.append(i)
for i in list3:  # 将序号填入字符串
    a = "字符{}出现了{}次".format(list1[i], b)
    set1.add(a)
list(set1)  # 将集合转化为列表
for i in set1:
    print(i)
