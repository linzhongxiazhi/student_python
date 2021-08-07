from tkinter import *
import  tkinter.messagebox

"""lb2是存入密码功能"""
lb2 = Tk()
lb2.title("个人密码管理系统")
# 创建一个居中的窗口
sw2 = lb2.winfo_screenwidth()
sh2 = lb2.winfo_screenheight()
ww2 = 450
wh2 = 300
x2 = (sw2-ww2) / 2
y2 = (sh2-wh2) / 2
lb2.geometry("%dx%d+%d+%d" %(ww2,wh2,x2,y2))
lb2.resizable(0, 0)  # 设置窗口大小不可变
"""元素"""
lb2.title("个人密码管理系统")
lb2.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico")
headline = Label(lb2,text='存入密码',fg='red',font=('黑体',12),width=20,height=2,).pack()#bg='#d3fbfb',relief=GROOVE
Label(lb2, text='输入平台：').place(x=100,y=60)
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
enter_usr_password = Entry(lb2, textvariable=var_usr_password,  show='*').place(x=180, y=140)
# 确认密码
var_usr_password2 = StringVar()
enter_usr_password2 = Entry(lb2, textvariable=var_usr_password2,  show='*').place(x=180, y=180)


# 按钮创建
def enter():
    usr_terrace =var_usr_terrace.get()
    usr_name1 =var_usr_name1.get()
    usr_password =var_usr_password.get()
    usr_password2 =var_usr_password2.get()
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


enter = Button(lb2,text="确认",fg="green",font=("黑体,12"),width=10,height=1,cursor="shuttle",command=enter).place(x=190, y=220)


lb2.mainloop()