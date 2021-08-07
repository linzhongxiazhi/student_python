from tkinter import *
from tkinter import messagebox
import hashlib

root = Tk()
root.title("注册窗口演示")
root.geometry("400x250")
root.resizable(0, 0)
f1 = Frame(root)
f1.pack()
l1 = Label(f1, text="用户名").grid(row=0, column=0)
l2 = Label(f1, text="输入密码").grid(row=1, column=0)
l2 = Label(f1, text="再次确认").grid(row=2, column=0)


def change():
    username.config(bg="white")
    return True


def change2():
    password.config(bg="white")
    return True


def change3():
    password_.config(bg="white")
    return True


username = Entry(f1, validate="focusin", validatecommand=change)
username.grid(row=0, column=1, pady=20)
password = Entry(f1, validate="focusin", validatecommand=change2)
password.grid(row=1, column=1)
password_ = Entry(f1, validate="focusin", validatecommand=change3)
password_.grid(row=2, column=1)


def register():
    if username.get() == "":
        username.config(bg="Crimson")
        messagebox.showerror("提示", "用户名不能为空")
    elif username.get() != "":
        f = open("账户信息.txt", mode="r", encoding="utf-8")
        information = f.readlines()
        DIC = {}
        for i in range(len(information)):
            DIC[information[i].split("\t")[0]] = information[i].split("\t")[1][0:-1]
        if username.get() in DIC.keys():
            messagebox.showerror("警告",message="当前用户名: {0}\n已被注册,请更换".format(username.get()))
        elif password.get() == "":
            messagebox.showerror("提示", "密码不能为空")
        elif password.get() != password_.get():
            password.config(bg="Crimson")
            password_.config(bg="Crimson")
            password_.delete(0, END)
            messagebox.showerror("提示", "两次密码输入不一致")
        elif password.get() == password_.get():
            m = hashlib.md5("欢乐海岸".encode("utf-8"))
            m.update(password.get().encode("utf-8"))
            f = open("D:\\账户信息.txt", mode="a", encoding="utf-8")
            f.write(username.get() + "\t" + m.hexdigest() + "\n")
            print(m.hexdigest())
            f.close()
            messagebox.showinfo("提示", "注册成功")


Button(f1, text="注册", width=10, command=register).grid(row=3, column=0, sticky=W, pady=5)
Button(f1, text="退出", width=10, command=root.quit).grid(row=3, column=1, sticky=E, pady=5)


def readinfo():
    f = open("账户信息.txt", mode="r", encoding="utf-8")
    information = f.readlines()

    D = {}

    for i in range(len(information)):
        D[information[i].split("\t")[0]] = information[i].split("\t")[1][0:-1]

    print(D)

    f.close()


Button(f1, text="读出账户信息", width=10, command=readinfo).grid(row=4, column=1, sticky=E, pady=5)

root.mainloop()