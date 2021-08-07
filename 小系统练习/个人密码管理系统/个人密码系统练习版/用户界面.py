from tkinter import *
import  tkinter.messagebox

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
def new_card():
    """lb2是存入密码功能"""
    global lb2
    lb2 = Tk()
    lb2.title("个人密码管理系统")
    # 创建一个居中的窗口
    sw2 = lb2.winfo_screenwidth()
    sh2 = lb2.winfo_screenheight()
    ww2 = 450
    wh2 = 300
    x2 = (sw2 - ww2) / 2
    y2 = (sh2 - wh2) / 2
    lb2.geometry("%dx%d+%d+%d" % (ww2, wh2, x2, y2))
    lb2.resizable(0, 0)  # 设置窗口大小不可变
    """元素"""
    lb2.title("个人密码管理系统")
    lb2.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico")
    headline = Label(lb2, text='存入密码', fg='red', font=('黑体', 12), width=20,
                     height=2, ).pack()  # bg='#d3fbfb',relief=GROOVE
    Label(lb2, text='输入平台：').place(x=100, y=60)
    Label(lb2, text='输入账号：').place(x=100, y=100)
    Label(lb2, text='输入密码：').place(x=100, y=140)
    Label(lb2, text='确认密码：').place(x=100, y=180)
    # 平台
    var_usr_terrace = StringVar()
    enter_usr_terrace = Entry(lb2, textvariable=var_usr_terrace).place(x=180, y=60)
    # 姓名
    var_usr_name1 = StringVar()
    enter_usr_name1 = Entry(lb2, textvariable=var_usr_name1, ).place(x=180, y=100)
    # 密码
    var_usr_password = StringVar()
    enter_usr_password = Entry(lb2, textvariable=var_usr_password, show='*').place(x=180, y=140)
    # 确认密码
    var_usr_password2 = StringVar()
    enter_usr_password2 = Entry(lb2, textvariable=var_usr_password2, show='*').place(x=180, y=180)

    # 按钮创建
    def enter12():
        usr_terrace = var_usr_terrace.get()
        usr_name1 = var_usr_name1.get()
        usr_password = var_usr_password.get()
        usr_password2 = var_usr_password2.get()
        if usr_password == usr_password2:
            pswd = usr_password
            passwordfile = open("password.txt", "a")
            sequence = "平台：" + usr_terrace + " " + \
                       "账号：" + usr_name1 + " " + \
                       "密码：" + pswd + "\n"
            passwordfile.write(sequence)
            passwordfile.close()
            tkinter.messagebox.showinfo(message='已录入！')
        else:
            tkinter.messagebox.showerror(message='两次密码输入不一样！')

    Button(lb2, text="确认", fg="green", font=("黑体,12"), width=10, height=1, cursor="shuttle", command=enter12).place(
        x=190, y=220)
    lb2.mainloop()
def show_all():
    """lb3是显示全部"""
    lb3 = Tk()
    # 创建一个居中的窗口
    sw3 = lb3.winfo_screenwidth()
    sh3 = lb3.winfo_screenheight()
    ww3 = 450
    wh3 = 300
    x3 = (sw3 - ww3) / 2
    y3 = (sh3 - wh3) / 2
    lb3.geometry("%dx%d+%d+%d" % (ww3, wh3, x3, y3))
    lb3.resizable(0, 0)  # 设置窗口大小不可变
    # 界面优化
    lb3.title("个人密码管理系统")
    lb3.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico")
    headline = Label(lb3, text='显示全部', fg='red', font=('黑体', 12), width=15,
                     height=2, ).pack()  # bg='#d3fbfb',relief=GROOVE
    # photo = PhotoImage(file='未标题-1.png')
    # canvas = Canvas(lb)
    # canvas.pack(side='top')
    # canvas.create_image(450, 450, image=photo)
    # 显示全部
    sb = Scrollbar(lb3)
    sb.pack(side="right", fill="y")
    sb2 = Scrollbar(lb3, orient=HORIZONTAL)
    sb2.pack(side="bottom", fill="x")

    t = Text(lb3, yscrollcommand=sb.set, xscrollcommand=sb2.set, wrap='none', width=100000, height=100000)
    t.pack()
    passwordfile2 = open("password.txt", "r+")
    for line in passwordfile2.readlines():
        line = line.strip() + "\n"
        print(line)
        t.insert("insert", str(line))

    passwordfile2.close()
    t.pack(side="left", fill="both")
    t.pack(side=LEFT, fill=BOTH)
    sb.config(command=t.yview)
    sb2.config(command=t.xview)

    lb3.mainloop()
def search_cardd():
    """lb4为查找密码"""
    lb4 = Tk()
    # 创建一个居中的窗口
    sw4 = lb4.winfo_screenwidth()
    sh4 = lb4.winfo_screenheight()
    ww4 = 450
    wh4 = 300
    x4 = (sw4 - ww4) / 2
    y4 = (sh4 - wh4) / 2
    lb4.geometry("%dx%d+%d+%d" % (ww4, wh4, x4, y4))
    lb4.resizable(0, 0)  # 设置窗口大小不可变
    # 界面优化
    lb4.title("个人密码管理系统")
    lb4.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico")
    headline = Label(lb4, text='查找密码', fg='red', font=('黑体', 12), width=15,
                     height=2, ).pack()  # bg='#d3fbfb',relief=GROOVE
    # photo = PhotoImage(file='未标题-1.png')
    # canvas = Canvas(lb)
    # canvas.pack(side='top')
    # canvas.create_image(450, 450, image=photo)

    # 查找框
    Label(lb4, text='请输入要查询的平台').place(x=120, y=87)
    var_search = StringVar()
    Entry(lb4, font=("黑体", 18), textvariable=var_search).place(x=100, y=50)
    sb1 = Scrollbar(lb4)
    sb1.pack(side="right", fill="y")
    sb21 = Scrollbar(lb4, orient=HORIZONTAL)
    sb21.pack(side="bottom", fill="x")
    t3 = Text(lb4, yscrollcommand=sb1.set, xscrollcommand=sb21.set, wrap='none', width=45, height=12)
    t3.place(x=65, y=120)
    # t3.pack(side="left", fill="both")
    # t3.pack(side=LEFT, fill=BOTH)
    sb1.config(command=t3.yview)
    sb21.config(command=t3.xview)

    # 按钮
    def find():
        # aa = []
        if var_search.get() == "":
            tkinter.messagebox.showerror(message='您还没有输入内容呢！')
        # else:
        #     def search_password():
        #         bb = []
        #         x = 0
        #         for i in aa:
        #             for j in i:
        #                 if var_search.get() in j:
        #                     x += 1
        #                     bb.append(j)
        #         if x==0:
        #             tkinter.messagebox.showinfo(message='没有查找到！')
        #         return bb
        #     with open("password.txt", "r") as f:
        #         for line in f.readlines():
        #             data = line.split('\n\t')
        #             for str in data:
        #                 sub_str = str.split(' ')
        #             if sub_str:
        #                 aa.append(sub_str)
        #     q = search_password()
        #     t3 = Text(lb4, width=15, height=10).place(x=150, y=150)
        else:
            passwordfile3 = open("password.txt", "r+")
            aaa = []
            x = 0
            for j in passwordfile3.readlines():
                r = j.strip() + "\n"
                if var_search.get() in j:
                    x += 1
                    t3.insert("insert", str(r))
            if x == 0:
                tkinter.messagebox.showinfo(message='没有查找到！')

    Button(lb4, text="查找", bg="green", font=("黑体", 12), command=find).place(x=280, y=85)

    lb4.mainloop()
# 按钮
new_card =Button(lb1,text="存入密码",fg="green",font=("黑体,12"),width=20,height=2,cursor="shuttle",command=new_card).place(x=140, y=50)
show_all =Button(lb1,text="显示全部",fg="green",font=("黑体,12"),width=20,height=2,cursor="shuttle",command=show_all).place(x=140, y=130)
search_card =Button(lb1,text="查询密码",fg="green",font=("黑体,12"),width=20,height=2,cursor="shuttle",command=search_cardd).place(x=140, y=210)

lb1.mainloop()
