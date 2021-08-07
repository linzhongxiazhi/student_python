# 九九乘法表打印
# 定义行计数器
row = 1
while row <= 9:

    # 定义列计数器
    col = 1
    while col <= row:
        print("{}*{}={}".format(row, col, row * col), end=" ")
        col += 1
    print()
    row += 1
