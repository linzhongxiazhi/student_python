from tkinter import *
lb4 =Tk()
for line in passwordfile2.readlines():
    line = line.strip()+"\n"
    print(line)
    t.insert("insert", str(line))