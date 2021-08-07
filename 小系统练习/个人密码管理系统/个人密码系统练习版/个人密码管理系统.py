from tkinter import *
import  tkinter.messagebox
#居中

sw = middle.winfo_screenwidth()
sh = middle.winfo_screenheight()
ww = 450
wh = 300
x = (sw - ww) / 2
y = (sh - wh) / 2
#创建一个登录界面
register =Tk()
register.geometry("%dx%d+%d+%d" % (ww, wh, x, y))







register.mainloop()