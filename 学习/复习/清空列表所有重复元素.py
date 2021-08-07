# 清空列表所有重复元素
a = [1, 2, 3, 4, 5, 6, 7, 1, 2, 1, 2, 1]
b = 1
while b in a:
    a.remove(b)
print(a)
