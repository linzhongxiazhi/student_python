from tkinter import *
import  tkinter.messagebox

"""lb3是显示全部"""
lb3 = Tk()
# 创建一个居中的窗口
sw3 = lb3.winfo_screenwidth()
sh3 = lb3.winfo_screenheight()
ww3 = 450
wh3 = 300
x3 = (sw3-ww3) / 2
y3 = (sh3-wh3) / 2
lb3.geometry("%dx%d+%d+%d" %(ww3,wh3,x3,y3))
lb3.resizable(0, 0)  # 设置窗口大小不可变
# 界面优化
lb3.title("个人密码管理系统")
lb3.wm_iconbitmap("vcard_128px_1159134_easyicon.net.ico")
headline = Label(lb3,text='显示全部',fg='red',font=('黑体',12),width=15,height=2,).pack()#bg='#d3fbfb',relief=GROOVE
# photo = PhotoImage(file='未标题-1.png')
# canvas = Canvas(lb)
# canvas.pack(side='top')
# canvas.create_image(450, 450, image=photo)
#显示全部
sb = Scrollbar(lb3)
sb.pack(side="right", fill="y")
sb2 =Scrollbar(lb3,orient=HORIZONTAL)
sb2.pack(side="bottom",fill="x")

t = Text(lb3, yscrollcommand=sb.set, xscrollcommand=sb2.set, wrap='none',width=100000,height=100000)
t.pack()
passwordfile2 =open("password.txt","r+")
for line in passwordfile2.readlines():
    line = line.strip()+"\n"
    print(line)
    t.insert("insert", str(line))

passwordfile2.close()
t.pack(side="left", fill="both")
t.pack(side=LEFT, fill=BOTH)
sb.config(command=t.yview)
sb2.config(command=t.xview)


lb3.mainloop()