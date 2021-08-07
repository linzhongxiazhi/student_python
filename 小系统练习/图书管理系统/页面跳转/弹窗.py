import tkinter as tk
import tkinter.messagebox
window =tk.Tk()

window.title("my window")
window.geometry("200x200")
def hit_me():
    # tk.messagebox.showinfo(title="hi",message="hahah")
    #tk.messagebox.showwarning(title="hi", message="nono")#警告
    #tk.messagebox.showerror(title="hi", message="错误")
    #tk.messagebox.askquestion(title="hi", message="hahah")#有返回值
    tk.messagebox.askyesno(title="hi", message="hahah")#turo or false
    # tk.messagebox.askokcancel(title="hi", message="hahah")
tk.Button(window,text="anjiu",command =hit_me).pack()
window.mainloop()