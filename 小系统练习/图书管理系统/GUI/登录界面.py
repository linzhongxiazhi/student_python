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

        lb.quit()
    else:
        tkinter.messagebox.showerror(message='账号或密码有错误！')
# 按钮创建
enter = Button(lb,text="登录",fg="green",font=("黑体,12"),width=10,height=2,cursor="shuttle",command=enter).place(x=180, y=200)
lb.mainloop()