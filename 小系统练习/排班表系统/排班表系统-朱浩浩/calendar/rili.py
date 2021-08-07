from tkinter import *
from tkinter.ttk import *
from lunar.lunar import Apps
from lunar.weather import AppWeather
import tkinter as tk
from datetime import *
import tkinter.font as tkFont
import time
##import requests as re
##import json
import lunar.Get_Api as GA

nameList=[i for i in range(1,43)]
valueList=[i for i in range(1,43)]
nameList0=[i for i in range(1,43)]
valueList0=["周一", "周二", "周三", "周四", "周五", "周六", "周天"]

class biao():
    def __init__(self,maxr,maxc):
        ''':param maxr:设置总行数
           :param maxc:设置字段数量'''
        self.maxr=maxr
        self.maxc=maxc
        global textList
        textList=locals()#自动生成变量名字典集
    def auto_Create_Text(self,father,namelist=None,valueList=None):
        ''':param father:父组件的名称
           :param namelist:表格的字段名称
           :param valuelist:字段名的值'''
        name=0
        for r in range(self.maxr):
            for c in range(self.maxc):
                name+=1 #设置表格编号如text00，text01
                textList[name]=tk.Label(father,bd='1',relief='solid')
                textList[name].place(relx=c/(self.maxc+0.1),rely=r/self.maxr,relwidth=0.15,relheight=0.175)
                if c%2 == 0:
                    textList[name].configure(text='')
                    textList[name].configure(bg='Gainsboro')
                else:
                    #设置字段值
                    textList[name].configure(text='')

class App:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("✽排班表 ❀")
        self.windows.geometry("646x600")
        self.font() 
        self.lis1 = ["周一", "周二", "周三", "周四", "周五", "周六", "周天"]
        self.images=[]
##        self.creat_image_lis()
        self.creat_res()
        self.default()
        self.windows.mainloop()
    def font(self):
        self.ft = tkFont.Font(family='粗体',size=15,weight=tkFont.BOLD)
    def refresh_time(self):
        while self.sw == 0:
            self.T2.config(text=f"{str(date.today())} {time.strftime('%H:%M:%S')}\n",bg='skyblue')
            self.windows.after(1,self.refresh_time)
            break
        
        
    def refresh(self):
        self.sw = 0
        self.jia1 = 0
        self.yi1 = 0
        self.bing1 = 0
        self.ding1 = 0
        self.jia2 = 0
        self.yi2 = 0
        self.bing2 = 0
        self.ding2 = 0
        self.jia3 = 0
        self.yi3 = 0
        self.bing3 = 0
        self.ding3 = 0
        self.jia4 = 0
        self.yi4 = 0
        self.bing4 = 0
        self.ding4 = 0
        self.refresh2()
    def refresh2(self):
        self.LF.destroy()
        self.LF = tk.LabelFrame(self.windows)
        self.LF.place(relx=10/430, rely=30/400, relwidth=285/430, relheight=165/400)
        a=biao(6,7)
        a.auto_Create_Text(self.LF,nameList,valueList)
    def default(self):
        self.sw = 0
        self.jia1 = 0
        self.yi1 = 0
        self.bing1 = 0
        self.ding1 = 0
        self.jia2 = 0
        self.yi2 = 0
        self.bing2 = 0
        self.ding2 = 0
        self.jia3 = 0
        self.yi3 = 0
        self.bing3 = 0
        self.ding3 = 0
        self.jia4 = 0
        self.yi4 = 0
        self.bing4 = 0
        self.ding4 = 0
        global today
        today = str(date.today())
        y = int(today.split('-')[0])
        m = int(today.split('-')[1].split('-')[0])
        d = int(today.split('-')[2])
        self.a = y
        self.b = m
##        self.h = 0 #获取假日默认月第几天
        self.func1()
        self.press_today()
        self.view_image()
    def func1(self):
        ## ==此处插入检查年份生成当年节假日{dictH}函数== ##
        global list1
        self.a = int(self.C1.get())
        list1 = GA.holiday(self.a)
##        print(list1)
##        print('---------')
        self.get_total_days(self.a, self.b)
        self.print_days(self.a, self.b, list1)
##    def creat_image_lis(self):
##        for i in range(1,13):
##            self.images.append("res/%s.png"%i)
    def view_image(self):
        pass
##        self.ima=PhotoImage(file=self.images[self.b-1])
##        self.L3.config(image=self.ima)
    def holiday(self,a):
        pass

    def go(self,*args):
        self.refresh()
        
        try:
            self.p = 1
            self.a = int(self.C1.get())  # 获取年份
            self.b = int(self.C2.get())  # 获取月份
            self.func1()
            self.view_image()
##            print(f'{self.C2.current()}')
        except Exception:
                pass
    def up(self,*args):
        if 0 < self.b < 13:
            try:
                self.refresh()
                self.a = int(self.C1.get())  # 获取年份
                self.b = int(self.C2.get()) - 1  # 获取月份
                self.func1()
                self.view_image()
            except Exception:
                pass
        if self.b == 0:
            self.a = int(self.C1.get()) - 1
            self.b = 12
            self.refresh()
            self.func1()
            self.view_image()
    def down(self,*args):
        if 0 < self.b < 13:
            try:
                self.refresh()
                self.a = int(self.C1.get())  # 获取年份
                self.b = int(self.C2.get()) + 1  # 获取月份
                self.func1()
                self.view_image()
            except Exception:
                pass
        if self.b == 13:
            self.a = int(self.C1.get()) + 1
            self.b = 1
            self.refresh()
            self.func1()
            self.view_image()

    def run_game(self):
        a1=Apps()
        if self.windows.quit():#如果主程序关闭
            Apps.windows.quit() #子程序关闭
    def weather(self):
        a21=AppWeather()
        if self.windows.quit():#如果主程序关闭
            Apps.windows.quit() #子程序关闭

    def creat_res(self):
        self.L1=Label(self.windows,text="年份:")
        self.L2=Label(self.windows,text="月份:")
        self.L3=Label(self.windows)
        self.B0 = Button(self.windows, text="上月", command=self.up)
        self.B0.place(relx=300/430, rely=60/400)
        self.B1 = tk.Label(self.windows, text="三倍节假日",activebackground='lightpink',takefocus=True,state='active')
        self.B1.place(relx=300/430, rely=85/430, relwidth=0.3, relheight=0.2)
        self.B2 = Button(self.windows, text="下月", command=self.down)
        self.B2.place(relx=370/430, rely=60/400)
        self.B3=Button(self.windows,text="农历",command=self.run_game)
        self.B3.place(relx=370/430, rely=191/400)
        self.B5=Button(self.windows,text="天气",command=self.weather)
        self.B5.place(relx=300/430, rely=191/400)
        self.B4 = tk.Button(self.windows, text="今天", command=self.press_today,bg='skyblue')
        self.B4.place(relx=300/430, rely=173/430, relwidth=0.3)
        self.temp1 = StringVar()
        self.temp2 = StringVar()
        self.sw = IntVar()
        self.sw = 0
        self.C1=Combobox(self.windows,values=[x for x in range(0,9999)])
        self.C1.current(int(str(date.today()).split('-')[0]))
        self.C1.bind('<<ComboboxSelected>>',self.go)
        self.C2=Combobox(self.windows,values=[x for x in range(0,13)])
        self.C2.current(int(str(date.today()).split('-')[1].split('-')[0])-1)
        self.C2.bind('<<ComboboxSelected>>',self.go)
        self.C1.place(relx=300/430, rely=30/430, relwidth=60/430, relheight=30/400)
        self.C2.place(relx=375/430, rely=28/400, relwidth=50/430, relheight=30/400)
        self.L1.place(relx=300/430, rely=0, relwidth=70/430, relheight=30/400)
        self.L2.place(relx=370/430, rely=0, relwidth=50/430, relheight=30/400)
        self.L3.place(relx=10/430, rely=195/430, relwidth=280/430, relheight=220/400)
        self.L4 = tk.LabelFrame(self.windows, text='统计信息：',bd=8)
        self.L4.place(relx=0.7, rely=0.55, relwidth=0.3, relheight=0.35)
        self.L4_1 = Label(self.L4, text='甲班 : 白8夜7休16')
        self.L4_1.place(relx=0, rely=0)
        self.L4_2 = Label(self.L4, text='乙班 : 白7夜8休16')
        self.L4_2.place(relx=0, rely=0.25)
        self.L4_3 = Label(self.L4, text='丙班 : 白8夜8休15')
        self.L4_3.place(relx=0, rely=0.5)
        self.L4_4 = Label(self.L4, text='丁班 : 白8夜8休15')
        self.L4_4.place(relx=0, rely=0.75)
        self.L5 = tk.Label(self.windows, text='作者：张伦\n联系电话：661731',bg='#DCDCDC',justify='left')
        self.L5.place(relx=0.7, rely=0.9, relwidth=0.29, relheight=0.08)
        self.LF0 = tk.LabelFrame(self.windows)
        self.LF0.place(relx=10/430, rely=3/400, relwidth=285/430, relheight=30/400)
        b=biao(1,7)
        b.auto_Create_Text(self.LF0,nameList0,valueList0)
        name0=0
        for i in valueList0:
            textList[name0+1].configure(text=f'{valueList0[name0]}')
            textList[name0+1].place(relheight=1)
            name0+=1
        self.LF = tk.LabelFrame(self.windows)
        self.LF.place(relx=10/430, rely=30/400, relwidth=285/430, relheight=165/400)
        a=biao(6,7)
        a.auto_Create_Text(self.LF,nameList,valueList)
        self.L6 = tk.Label(self.windows)
        self.L6.place(relx=9/430, rely=195/400, relwidth=287/430, relheight=34/400)
        self.T1 = tk.Label(self.L6,text="现在时间是：\n",bg='skyblue')
        self.T1.place(relx=0, rely=0, relwidth=1, relheight=0.8)
##        self.T1.insert(END, "今天是：\n")
        
        self.T2 = tk.Label(self.L6,font=self.ft,text=f"{str(date.today())} {time.strftime('%H:%M:%S')}\n",bg='skyblue')
        self.T2.place(relx=0, rely=0.4,relwidth=1, relheight=1)
        
##        self.T2.insert(END, f"{str(date.today())}\n")
        self.LF3 = tk.LabelFrame(self.windows,bg='lightblue')
        self.LF3.place(relx=10/430, rely=230/400, relwidth=285/430, relheight=163/400)
        self.T3 = tk.Text(self.LF3,font=self.ft,bg='lightblue')
        self.T3.place(relx=0, rely=0/400, relwidth=1, relheight=1)
        
        
    def content(self,day):
        print(day)
        self.T3.config(bg='palegreen')
        self.T3.delete(0.0,END)     # 清空T3板
        N=(self.i+day%7-1)%7
        print(f'self.i={self.i}')
        print(N)                    #星期N
        K=int((day+self.i-2)/7+1)
        print(K)                    #当月第K周
        self.T3.insert(END,f'{day}号是{self.b}月第{K}周的星期{N}\n\n')
        self.T3.insert(END,f'<当日日常作业内容>：\n')
        self.T3.insert(END,f'\t[每天]刮板正反转，冲洗底部\n')
        self.T3.insert(END,f'<当日周期性作业内容>：\n')
        if K == 2 or K ==3:
            if N == 2:
                self.T3.insert(END,f'\t[每月第二/三周周二]19E01切换\n')
        if N == 1:
            self.T3.insert(END,f'\t[每周一]清理中控收集铁桶内切片\n')
            self.T3.insert(END,f'\t[每周一、四]清理35筛网\n')
        if N == 3:
            self.T3.insert(END,f'\t[每周三]清理磁力架\n')
            self.T3.insert(END,f'\t[每周三]疏通17024、15024/15019引压管\n')
        if N == 4:
            self.T3.insert(END,f'\t[每周四]工艺参数检查\n')
            self.T3.insert(END,f'\t[每周四]10/20取样分析\n')
            self.T3.insert(END,f'\t[每周一、四]清理35筛网\n')
        if N == 5:
            self.T3.insert(END,f'\t[每周五]工艺联锁检查\n')
        if N == 1 or N == 3 or N == 5:
            self.T3.insert(END,f'\t[每周一、三、五]清洗19水箱\n')
        if day == 1:
            self.T3.insert(END,f'\t[每月1号]清洗三个热井收集箱滤网\n')
        if day == 1 or day == 15:
            self.T3.insert(END,f'\t[每月1/15号]冲洗17J01第一级\n')
        if day == 2 or day == 16:
            self.T3.insert(END,f'\t[每月2/16号]冲洗17J01第二级\n')
        if day == 3 or day == 17:
            self.T3.insert(END,f'\t[每月3/17号]冲洗17J01第三级\n')
        if day == 5:
            self.T3.insert(END,f'\t[每月5号]动设备切换\n')
        if day == 7 or day == 17 or day == 27:
            self.T3.insert(END,f'\t[每月7/17/27号]标定料仓\n')
        if self.b%2 ==1:
            if day==14 or day==15 or day==16:
                self.T3.insert(END,f'\t[每单数月14-16号]切换除盐水总管\n')
        if self.b==1 or self.b==4 or self.b==7 or self.b==11:
            if day==19 or day==20 or day==21:
                self.T3.insert(END,f'\t[1/4/7/11月的19-21号]切换拆洗85F04/05\n')
##        self.T3.config(state='disabled')
    def press_today(self):
        self.refresh()
        
        self.a = int(today.split('-')[0])  # 获取年份
        self.b = int(today.split('-')[1].split('-')[0])  # 获取月份
##        self.h = 2  #获取假日当月第几天
        self.func1()
        self.T1.config(text="现在时间是：\n",bg='skyblue')
        self.T2.config(text=f"{str(date.today())} {time.strftime('%H:%M:%S')}\n",bg='skyblue')
        self.refresh_time()
        print('是今天')
        self.content(int(today.split('-')[2]))
        self.view_image()
        self.T3.config(bg='lightblue')
        pass
        pass
    def day_Selected(self,day=None):
        today = str(date.today())
        if day==int(today.split('-')[2]) and self.C1.current()==int(today.split('-')[0]) and self.C2.current()==int(today.split('-')[1].split('-')[0]):
            self.sw = 0
            self.T1.config(text="现在时间是：\n",bg='skyblue')
            self.T2.config(text=f"{str(date.today())} {time.strftime('%H:%M:%S')}\n",bg='skyblue')
            self.refresh_time()
            textList[day+self.i-1].config(bg='skyblue')
##            print('是今天')
            self.content(day)
            self.T3.config(bg='lightblue')
            pass
        else:
            self.sw = 1
            self.L6.destroy()
            self.L6 = tk.Label(self.windows)
            self.L6.place(relx=9/430, rely=195/400, relwidth=287/430, relheight=34/400)
            self.T1 = tk.Label(self.L6,text="当前选择：\n",bg='lightgreen')
            self.T1.place(relx=0, rely=0, relwidth=1, relheight=0.8)
            self.T2 = tk.Label(self.L6,font=self.ft,text=f"{self.a}年{self.b}月{day}号\n",bg='lightgreen')
            self.T2.place(relx=0, rely=0.4,relwidth=1, relheight=1)
            self.content(day)
        pass
    def press(self,event,num):
        day=num[0]-self.i+2
        textList[num[0]+1].config(bg='lightgreen',bd=2)
        self.day_Selected(day)
        pass
    def press_right(self,event,num):

        day=num[0]-self.i+2
        pop_x=event.x_root
        pop_y=event.y_root
        self.top=tk.Toplevel(bd=1,relief='solid')
        self.top.geometry("%dx%d+%d+%d" % (220, 180, pop_x, pop_y))
        self.top.overrideredirect(True)
        self.tempE=Text(self.top,bg='lightgreen')
        self.tempE.place(relx=0,rely=0,relwidth=1,relheight=1)
        self.tempE.insert(END,f'当前选择{self.a}年{self.b}月{day}号\n')
        self.tempE.insert(END,f'------------------------------\n待办事项：\n')
        pass
    def out(self,*args):
        self.top.destroy()
        print('111')
        pass
    def leap_year(self,a):#a 不能用self.a
        if (a % 4 == 0 and a % 100 != 0) or a % 400 == 0:
            return True     #判断是闰年
        else:
            return False    #判断不是闰年
    def year_days(self,a,b):#year_days b不能用self.b
        if b in (1,3,5,7,8,10,12):
            # days=31
            return 31
        elif b in (4,6,9,11):
            # days=30
            return 30
        else:
            if self.leap_year(self.a)==True:
                # days=29
                return 29   #闰年的2月有29天
            else:
                # days=28
                return 28
    def get_total_days(self,a,b):
        total_days=0
        for m in range(1900,self.a):
            # print(m,self.leap_year(m))
            if self.leap_year(m)==True:
                total_days+=366
            else:
                total_days+=365
        # print("奶粉",total_days)
        for i in range(1,self.b):
            total_days+=self.year_days(self.a,i)
            # s=self.year_days(self.a,i)
            # print(s,s)
        return total_days

    def get_week(self,a,b):  # 计算从星期几开始
        return self.get_total_days(self.a,self.b)%7+1  # 计算从星期几开始

    def print_days(self,a,b,list1):
        self.C1.current(self.a)
        self.C2.current(self.b)
        self.i=self.get_week(self.a,self.b)
        lis1=[]
        lis1=[x for x in range(1,self.year_days(self.a,self.b)+1)] # 生成list1（1，2，...，当月总天数days）
##        print(lis1)
        day1=self.get_total_days(self.a,self.b)
        # ↓lis11表示当月每天距离1900/1/1的天数列表
        # ↓与Excel日期格式对不上是因为1900/2/29有BUG，是不存在的一天
        lis11=[]
        lis11=[l for l in range(day1+1,1+day1+self.year_days(self.a,self.b))]
##        print(lis11)
        '''↓↓↓处理班次序列↓↓↓'''
        lis21=lis11[:]
        for i in range(len(lis21)):
            if lis21[i]%4==1:
                lis21[i]='甲/丁'
            elif lis21[i]%4==2:
                lis21[i]='乙/甲'
            elif lis21[i]%4==3:
                lis21[i]='丙/乙'        
            elif lis21[i]%4==0:
                lis21[i]='丁/丙'
        '''↑↑↑处理班次序列↑↑↑'''
        for o in lis11:
            if o%4==0:
                self.jia1+=1
                self.ding2 += 1
                self.bing3 += 1
                self.yi4 += 1
            if o%4==1:
                self.yi1+=1
                self.jia2 += 1
                self.ding3 += 1
                self.bing4 += 1
            if o%4==2:
                self.bing1+=1
                self.yi2 += 1
                self.jia3 +=1
                self.ding4 += 1
            if o%4==3:
                self.ding1+=1
                self.bing2 += 1
                self.yi3 += 1
                self.jia4 += 1
        self.L4_1.config(text='甲班：白%s夜%s休%s' % (self.jia1,self.jia2,self.jia3+self.jia4))
        self.L4_2.config(text='乙班：白%s夜%s休%s' % (self.yi1, self.yi2, self.yi3 + self.yi4))
        self.L4_3.config(text='丙班：白%s夜%s休%s' % (self.bing1, self.bing2, self.bing3 + self.bing4))
        self.L4_4.config(text='丁班：白%s夜%s休%s' % (self.ding1, self.ding2, self.ding3 + self.ding4))
        for m in range(1,self.i):                       # self.i为月第一天星期几
            lis1.insert(0,"  ")                         # 空白文本       
            lis21.insert(0,"  ")
        if self.a==int(today.split('-')[0]) and self.b == int(today.split('-')[1].split('-')[0]):       #高亮今天
            m = len(range(self.i))
            day_today = int(today.split('-')[2])+m-1
            textList[day_today].configure(bg='skyblue')
        name=0
##        textList[self.i+self.h].configure(activebackground='lightpink',takefocus=True,state='active')
        for index,item in enumerate (lis1):
            if index > self.i-2:
                '''↓↓↓向Label插入信息↓↓↓'''
                textList[name+1].configure(text=f'{lis1[name]}\n{lis21[name]}')
##                textList[name+1].configure(text=f'{lis11[name]}\n{lis21[name]}')
                temp=textList[name+1]
                temp.bind("<Button-1>",lambda event,arg=[name]:self.press(event,arg))
                temp.bind("<Button-3>",lambda event,arg=[name]:self.press_right(event,arg))
                temp.bind("<ButtonRelease-3>",self.out)
            name+=1
            '''↑↑↑向Label插入信息↑↑↑'''
        if list1:
            for index,item in enumerate (list1):
    ##            print(list1[item])
                if list1[item] in lis11:
    ##                print('是在列表里')
    ##                print(lis11.index(list1[item]))
                    temp2=textList[lis11.index(list1[item])+self.i]
                    temp2.configure(bg='lightpink')
        else:
            self.B1.config(text=f'无网络或\n节假日API用完了')
if __name__ == '__main__':
    ap=App()
