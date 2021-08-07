# 自动轨迹绘制
import turtle as t

t.title("自动轨迹绘制")  # 标题
t.setup(400, 400, 0, 0)  # 窗口大小
t.pensize(5)  # 画笔粗度
t.pencolor("red")  # 画笔颜色
# 　数据读取
datals = []  # 定义一个列表
f = open("d:\\桌面\\data.txt")  # 打开一个txt文件
for line in f:
    line = line.replace("\n", "")
    datals.append(list(map(eval, line.split(","))))
f.close()
# 自动绘制
for i in range(len(datals)):  # 遍历文件data中的每一行
    t.pencolor(datals[i][3], datals[i][4], datals[i][5])  # 根据文件给的颜色来定义
    t.fd(datals[i][0])  # 根据文件给的距离来绘制
    if datals[i][1] == 1:  # 判断是不是左转
        t.right(datals[i][2])
    else:  # 判断是不是右转
        t.left(datals[i][2])
t.done()  # 保留画面窗口
