from tkinter import *
import tkinter.messagebox
"""登录窗口"""
register = Tk()
sw = register.winfo_screenwidth()
sh = register.winfo_screenheight()
ww = 450
wh = 300
x = (sw-ww) / 2
y = (sh-wh) / 2
register.geometry("%dx%d+%d+%d" %(ww,wh,x,y))
register.resizable(0, 0)  # 设置窗口大小不可变
register.title("个人密码管理系统 作者：朱浩浩") # 小标题
register.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico") #小图标
Label(register,text='用户登录界面',fg='red',font=('黑体',32),width=15,height=2,).pack()#大标题
"""元素"""
Label(register, text='账户：').place(x=100,y=100)
Label(register, text='密码：').place(x=100, y=140)
# 用户名
name = StringVar()
Entry(register, textvariable=name).place(x=180, y=100)
# 密码
password = StringVar()
Entry(register, textvariable=password, show='*').place(x=180, y=140)

# 登录按钮
def register_two():
    usr_name =name.get()
    usr_pwd =password.get()
    if usr_name == '' or usr_pwd == '':
        tkinter.messagebox.showerror(message='用户名或密码不能为空！')
    elif usr_name =="admin" and usr_pwd =="123456":
        register.destroy()#关闭登录窗口，进入菜单界面

        """打开一个居中的菜单界面"""
        menu =Tk()
        sw = menu.winfo_screenwidth()
        sh = menu.winfo_screenheight()
        ww = 450
        wh = 300
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        menu.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        menu.resizable(0, 0)  # 设置窗口大小不可变
        menu.title("个人密码管理系统 作者：朱浩浩")  # 小标题
        menu.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico")  # 小图标
        Label(menu, text='菜单', fg='red', font=('黑体', 32), width=15, height=2, ).pack()  # 大标题
        """创建菜单选项"""
        def new_pa():
            """居中存入密码"""
            # menu.destroy()
            newpa =Toplevel()
            sw = newpa.winfo_screenwidth()
            sh = newpa.winfo_screenheight()
            ww = 450
            wh = 300
            x = (sw - ww) / 2
            y = (sh - wh) / 2
            newpa.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
            newpa.resizable(0, 0)  # 设置窗口大小不可变
            newpa.title("个人密码管理系统 作者：朱浩浩")  # 小标题
            newpa.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico")  # 小图标
            Label(newpa, text='存入密码', fg='red', font=('黑体', 18), width=15, height=2, ).pack()  # 大标题
            """文本框"""
            #平台
            Label(newpa, text='输入平台：').place(x=100, y=60)
            var_pintai=StringVar()
            Entry(newpa, textvariable=var_pintai).place(x=180, y=60)
            #账号
            Label(newpa, text='输入账号：').place(x=100, y=100)
            var_zhanghao = StringVar()
            Entry(newpa, textvariable=var_zhanghao).place(x=180, y=100)
            #密码
            Label(newpa, text='输入密码：').place(x=100, y=140)
            var_mima = StringVar()
            Entry(newpa, textvariable=var_mima,show="*").place(x=180, y=140)
            #确认密码
            Label(newpa, text='确认密码：',).place(x=100, y=180)
            var_mima2 = StringVar()
            Entry(newpa, textvariable=var_mima2,show="*").place(x=180, y=180)
            #确认按钮
            def ok():
                if var_mima.get()=="" or var_mima2.get()=="":
                    tkinter.messagebox.showerror(message='您还没有输入密码呢！')
                elif var_mima.get() == var_mima2.get():
                    passwordfile = open("password.txt", "a")
                    str_line = "平台：" + var_pintai.get() + " " + \
                               "账号：" + var_zhanghao.get() + " " + \
                               "密码：" + var_mima.get() + "\n"
                    passwordfile.write(str_line)
                    passwordfile.close()
                    tkinter.messagebox.showinfo(message='已录入！')
                else:
                    tkinter.messagebox.showerror(message='两次密码输入不一样！')

            Button(newpa,text="确认",fg="green",font=("黑体,12"),width=10,height=2,cursor="shuttle",command=ok).place(x=180, y=220)
            newpa.mainloop()
        def show_all():
            """lb3是显示全部"""
            lb3 = Toplevel()
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
            lb3.title("个人密码管理系统 作者：朱浩浩")
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
        def search_pa():
            """lb4为查找密码"""
            lb4 = Toplevel()
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
            lb4.title("个人密码管理系统 作者：朱浩浩")
            lb4.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico")
            headline = Label(lb4, text='查找密码', fg='red', font=('黑体', 12), width=15,
                             height=2, ).pack()  # bg='#d3fbfb',relief=GROOVE
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
        a = Button(menu, text="存入密码", fg="green", font=("黑体,12"), width=10, height=2, cursor="shuttle",command=new_pa).place(x=155, y=80)
        b = Button(menu, text="显示全部", fg="green", font=("黑体,12"), width=10, height=2, cursor="shuttle",command=show_all).place(x=155, y=150)
        c = Button(menu, text="查询密码", fg="green", font=("黑体,12"), width=10, height=2, cursor="shuttle",command=search_pa).place(x=155, y=220)
        menu.mainloop()
    else:
        tkinter.messagebox.showerror(message='账号或密码有错误！')
Button(register,text="登录",fg="green",font=("黑体,12"),width=10,height=2,cursor="shuttle",command=register_two).place(x=180, y=200)
register.mainloop()