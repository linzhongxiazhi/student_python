# 升序 降序
list1 = eval(input("请输入一个列表:"))
list1.sort()
print("列表的升序为{}\n列表的降序为{}".format(list1,list1[::-1]))



'''
# 列表排序|去重
# 列表的排序:
# 升序sort() sorted()
a = [1, 3, 5, 2, 6]
a.sort()
print(a)
# =================
a = [1, 3, 5, 2, 6]
a_sorted = sorted(a)
print(a_sorted)
# 降序 [::-1] reverse()
a = [1, 3, 5]
a_list = a[::-1]
print(a_list)
# =================
a = [1, 3, 5]
a.reverse()
print(a)
# 列表去重
# 使用for循环进行去重
a = [1, 1, 2, 3]
a_list = []
for i in a:
if i not in a_list:
a_list.append(i)
print(a_list)
# 使用list(set())进行去重
a = [1, 3, 3, 5]
a_list = list(set(a))
print(a_list)
'''
