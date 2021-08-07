import sxtwl
from datetime import *
from tkinter import *

ymc = [u"十一", u"十二", u"正", u"二", u"三", u"四", u"五", u"六", u"七", u"八", u"九", u"十"]
rmc = [u"初一", u"初二", u"初三", u"初四", u"初五", u"初六", u"初七", u"初八", u"初九", u"初十",
               u"十一", u"十二", u"十三", u"十四", u"十五", u"十六", u"十七", u"十八", u"十九",
               u"二十", u"廿一", u"廿二", u"廿三", u"廿四", u"廿五", u"廿六", u"廿七", u"廿八", u"廿九", u"三十", u"卅一"]
lunar = sxtwl.Lunar()  # 实例化日历库
class Apps:
    def __init__(self):
        self.windows = Tk()

        self.windows.title("农历")
        sw = self.windows.winfo_screenwidth()
        sh = self.windows.winfo_screenheight()
        ww = 300
        wh = 150
        x = (sw - ww) / 2
        y = (sh - wh) / 2
        self.windows.geometry("%dx%d+%d+%d" % (ww, wh, x, y))
        self.creat_res()
        self.windows.mainloop()

    def creat_res(self):
        today = str(date.today())
        print(today)
        y = today.split('-')[0]
        print(y)
        m = today.split('-')[1].split('-')[0]
        print(m)
        d = today.split('-')[2]
        print(d)
        day = lunar.getDayBySolar(int(y), int(m), int(d))
        print(u"公历:", day.y, u"年", day.m, u"月", day.d, u"日")
        self.T1 = Text(self.windows)
        self.T1.place(x=10, y=8, width=150, height=20)
        self.T2 = Text(self.windows)
        self.T2.place(x=10, y=28, width=280, height=100)
        self.T2.insert(END, "*2021.4.18 排班表系统1.0\n")
        if day.Lleap:
            self.T1.delete(0.0, END)
            print(u"阴历:润", ymc[day.Lmc], u"月", rmc[day.Ldi], u"日")
            self.T1.insert(END, "阴历:润 %s月%s日" % (ymc[day.Lmc], rmc[day.Ldi]))
        else:
            self.T1.delete(0.0, END)
            print(u"阴历:", ymc[day.Lmc], u"月", rmc[day.Ldi], u"日")
            self.T1.insert(END, "阴历: %s月%s日" % (ymc[day.Lmc], rmc[day.Ldi]))





