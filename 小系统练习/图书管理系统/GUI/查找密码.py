from tkinter import *
import  tkinter.messagebox
"""lb4为查找密码"""
lb4 = Tk()
# 创建一个居中的窗口
sw4 = lb4.winfo_screenwidth()
sh4 = lb4.winfo_screenheight()
ww4 = 450
wh4 = 300
x4 = (sw4-ww4) / 2
y4 = (sh4-wh4) / 2
lb4.geometry("%dx%d+%d+%d" %(ww4,wh4,x4,y4))
lb4.resizable(0, 0)  # 设置窗口大小不可变
# 界面优化
lb4.title("个人密码管理系统")
lb4.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico")
headline = Label(lb4,text='查找密码',fg='red',font=('黑体',12),width=15,height=2,).pack()#bg='#d3fbfb',relief=GROOVE
#查找框
Label(lb4, text='请输入要查询的平台').place(x=120, y=87)
var_search = StringVar()
Entry(lb4,font=("黑体",18),textvariable=var_search).place(x=100,y=50)
sb1 = Scrollbar(lb4)
sb1.pack(side="right", fill="y")
sb21 =Scrollbar(lb4,orient=HORIZONTAL)
sb21.pack(side="bottom",fill="x")
t3 = Text(lb4, yscrollcommand=sb1.set, xscrollcommand=sb21.set,  wrap='none', width=45, height=12)
t3.place(x=65, y=120)
# t3.pack(side="left", fill="both")
# t3.pack(side=LEFT, fill=BOTH)
sb1.config(command=t3.yview)
sb21.config(command=t3.xview)
#按钮
def find():
    # aa = []
    if var_search.get() =="":
        tkinter.messagebox.showerror(message='您还没有输入内容呢！')
    else:
        passwordfile3 = open("password.txt", "r+")
        aaa = []
        x = 0
        for j in passwordfile3.readlines():
            r = j.strip() + "\n"
            if var_search.get() in j:
                x += 1
                t3.insert("insert", str(r))
        if x ==0:
            tkinter.messagebox.showinfo(message='没有查找到！')
Toplevel(lb4,text="查找",bg="green",font=("黑体",12),command=find).place(x=280,y=85)
lb4.mainloop()