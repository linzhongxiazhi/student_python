from itertools import combinations


def getinput(): #定义一个函数 获得用户输入
    num = input('请输入5个整数（大于等于1小于等于10），并用空格分开') # 用户输入
    global ls  # 定义ls 是全局变量
    ls = num.split()  # 根据空格生成一个列表赋值给变量 ls
    ls = list(map(int, ls)) # 将变量字符串转化为整行
    ls = list(set(ls)) #将列表转化为集合去重在转化为列表
    numbers = range(1, 11) #一个[1,10]的数组赋值给变量
    if set(ls).issubset(set(numbers)) == False or len(ls) != 5:  #
        getinput()


getinput()  # 运行函数
lssum = sum(ls)  #求和列表
comb = list(combinations(ls, 3))
flag = 1  # 变量赋值1
for i in comb:
    if (i[0] + i[1] + i[2]) % 10 == 0:
        print('{}+{}+{}={}'.format(i[0], i[1], i[2], sum(i)))
        print('另外两数字和为{}'.format(lssum - sum(i)))
        flag = 0
if flag == 1:
    print(sorted(ls))

