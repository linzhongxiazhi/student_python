list1 = eval(input("输入一个列表:"))  #　获得用户输入
num1 = eval(input("输入:"))  #获得用户输入
list2 = []  #　定义一个空列表
for i in list1:  # 遍历一遍用户输入
    for y in list1:  # 遍历一遍用户输入
        if y == i:  # 如果 y==i则跳出当次循环
            continue
        else:  # 不等于则
            if i + y == num1:  # 判断 i + y 是否等于 rargrt
                list2.append(i)  # 是的话则向列表添加 i 和y
                list2.append(y)
                break  # 跳出当前循环
print(list2)