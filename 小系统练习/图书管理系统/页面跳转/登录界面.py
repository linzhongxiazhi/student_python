from tkinter import *



# 创建根窗口，并添加组件
root = Tk()
root.title('名片管理系统')
root.resizable(0, 0)  # 设置窗口大小不可变
lb = Label(root,text='用户登录界面',bg='#d3fbfb',fg='red',font=('华文新魏',32),width=15,height=2,relief=GROOVE)  # 标签页
lb.pack()
canvas = Canvas(root)
canvas.pack(side='top')
# 创建标签
canvas.create_window(100, 50, window=Label(root, font=('宋体', 10), text='用户名', justify='left', padx=5, pady=4))
canvas.create_window(100, 90, window=Label(root, font=('宋体', 10), width=5, text='密码', justify='left', padx=5, pady=4))
# 账号密码输入框
user = canvas.create_window(210, 50, window=Entry(root, borderwidth=3))
password = canvas.create_window(210, 90, window=Entry(root, borderwidth=3, show='*'))
# 创建画布背景图
photo = PhotoImage(file='../GUI/未标题-1.png')
canvas.create_image(200, 150, image=photo)
# 创建按钮
canvas.create_window(190, 200, window=Button(root, width=15, bg='#87CEEB', text='立即登录'))
# 复选框

# 登录用户检查
# def loginCheck(self):
#     name = self.username.get()
#     secret = self.password.get()
#     if name == 'admin' and secret == '123456':
#         self.page.destroy()
#         MainPage(self.root)
#     else:
#         showinfo(title='错误', message='账号或密码错误！')
#
mainloop() 