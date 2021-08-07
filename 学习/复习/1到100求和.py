# # 1 到100求和
# #定义计数器
# i = 1
# #定义总和
# r = 0
# while i <= 100:
#     a = r
#     r += i
#     print("进行到第{}计算:{}+{}={}".format(i,i,a,r))
#     i += 1
#
# print("1到100总和为:{}".format(r))


""" 1到100偶数和 """
# 定义计数器
i = 1
c = 1
# 定义总和
r = 0
while i <= 100:
    if i % 2 == 0:
        i += 1
        continue
    else:
        a = r
        r += i
        print("进行到第{}计算:{}+{}={}".format(c, i, a, r))
        c += 1
        i += 1

print("1到100总和为:{}".format(r))
