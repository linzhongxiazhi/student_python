from tkinter import *
import  tkinter.messagebox

lb = Tk()
# 创建一个居中的窗口
sw = lb.winfo_screenwidth()
sh = lb.winfo_screenheight()
ww = 450
wh = 300
x = (sw-ww) / 2
y = (sh-wh) / 2
lb.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
lb.resizable(0, 0)  # 设置窗口大小不可变
# 界面优化
lb.title("个人密码管理系统")
lb.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico")
headline = Label(lb,text='用户登录界面',fg='red',font=('黑体',32),width=15,height=2,).pack()#bg='#d3fbfb',relief=GROOVE
# photo = PhotoImage(file='未标题-1.png')
# canvas = Canvas(lb)
# canvas.pack(side='top')
# canvas.create_image(450, 450, image=photo)
"""元素"""
Label(lb, text='账户：').place(x=100,y=100)
Label(lb, text='密码：').place(x=100, y=140)
# 用户名
var_usr_name = StringVar()
enter_usr_name = Entry(lb, textvariable=var_usr_name).place(x=180, y=100)
# 密码
var_usr_pwd = StringVar()
enter_usr_pwd = Entry(lb, textvariable=var_usr_pwd, show='*').place(x=180, y=140)

# 登录功能
def enter():
    usr_name = var_usr_name.get()
    usr_pwd = var_usr_pwd.get()
    if usr_name == '' or usr_pwd == '':
        tkinter.messagebox.showerror(message='用户名或密码不能为空！')
    elif usr_name =="admain" and usr_pwd =="123456":
        lb1 = Tk()
        lb1.title("名片管理系统")
        # 创建一个居中的窗口
        sw1 = lb1.winfo_screenwidth()
        sh1 = lb1.winfo_screenheight()
        ww1 = 450
        wh1 = 300
        x1 = (sw1 - ww1) / 2
        y1 = (sh1 - wh1) / 2
        lb1.geometry("%dx%d+%d+%d" % (ww1, wh1, x1, y1))
        lb1.resizable(0, 0)  # 设置窗口大小不可变
        # 元素
        lb1.title("密码管理系统")
        lb1.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico")
        headline = Label(lb1, text='欢迎使用个人密码管理系统', fg='red', font=('黑体', 12), width=25,
                         height=2, ).pack()  # bg='#d3fbfb',relief=GROOVE

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

            Button(lb2, text="确认", fg="green", font=("黑体,12"), width=10, height=1, cursor="shuttle",
                   command=enter12).place(
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

        # 按钮
        new_card = Button(lb1, text="存入密码", fg="green", font=("黑体,12"), width=20, height=2, cursor="shuttle",
                          command=new_card).place(x=140, y=50)
        show_all = Button(lb1, text="显示全部", fg="green", font=("黑体,12"), width=20, height=2, cursor="shuttle",
                          command=show_all).place(x=140, y=130)
        search_card = Button(lb1, text="查询密码", fg="green", font=("黑体,12"), width=20, height=2, cursor="shuttle",
                             command=search_cardd).place(x=140, y=210)

        lb1.mainloop()
        lb.quit()
    else:
        tkinter.messagebox.showerror(message='账号或密码有错误！')
# 按钮创建
enter = Button(lb,text="登录",fg="green",font=("黑体,12"),width=10,height=2,cursor="shuttle",command=enter).place(x=180, y=200)
lb.mainloop()