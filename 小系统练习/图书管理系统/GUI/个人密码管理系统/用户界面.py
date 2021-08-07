from tkinter import *
import  tkinter.messagebox
import Tools

lb1 = Tk()
lb1.title("名片管理系统")
# 创建一个居中的窗口
sw1 = lb1.winfo_screenwidth()
sh1 = lb1.winfo_screenheight()
ww1 = 450
wh1 = 300
x1 = (sw1-ww1) / 2
y1 = (sh1-wh1) / 2
lb1.geometry("%dx%d+%d+%d" %(ww1,wh1,x1,y1))
lb1.resizable(0, 0)  # 设置窗口大小不可变
# 元素
lb1.title("密码管理系统")
lb1.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico")
headline = Label(lb1,text='欢迎使用个人密码管理系统',fg='red',font=('黑体',12),width=25,height=2,).pack()#bg='#d3fbfb',relief=GROOVE
# 钮功能实现
# 按钮
new_card =Button(lb1, text="存入密码", fg="green", font=("黑体,12"), width=20, height=2, cursor="shuttle", command=Tools.new_pa()).place(x=140, y=50)
show_all =Button(lb1,text="显示全部",fg="green",font=("黑体,12"),width=20,height=2,cursor="shuttle",command=show_all).place(x=140, y=130)
search_card =Button(lb1,text="查询密码",fg="green",font=("黑体,12"),width=20,height=2,cursor="shuttle",command=search_cardd).place(x=140, y=210)

lb1.mainloop()