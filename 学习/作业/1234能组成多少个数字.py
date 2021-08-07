# 1234能组成多少个数字1.0 强算法
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9,]
list2= []

for i in list1:
    a = 100 * i  # 百位
    for x in list1:
        if x == i:
            continue
        else:
            b = 10 * x  # 十位
        for y in list1:
            if y == x:
                continue
            elif y == i:
                continue
            else:
                c = 1 * y  # 个位
                d = a + b + c
                list2.append(d)

print("一共有{}种可能".format(len(list2)))
print("分别为:\n{}".format(list2))
