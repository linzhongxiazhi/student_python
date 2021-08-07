# def greet_user(name):
#     print("你好呀,{}.".format(name))
# greet_user("朱浩浩")

"""8-1 消息：编写一个名为 display_message()的函数，它打印一个句子，指出你在本
章学的是什么。调用这个函数，确认显示的消息正确无误。"""
# def display_message():
#     print("本章学的是函数.")
#
# display_message()

"""8-2 喜欢的图书：编写一个名为 favorite_book()的函数，其中包含一个名为 title
的形参。这个函数打印一条消息，如 One of my favorite books is Alice in Wonderland。
调用这个函数，并将一本图书的名称作为实参传递给它。"""
# def favorite_book(title):
#     print("One of my favorite books is {}.".format(title))
# favorite_book("西游记")

"""8-3 T 恤：编写一个名为 make_shirt()的函数，它接受一个尺码以及要印到 T 恤上
的字样。这个函数应打印一个句子，概要地说明 T 恤的尺码和字样。
使用位置实参调用这个函数来制作一件 T 恤；再使用关键字实参来调用这个函数。"""
# def make_shirt(cm,zy):
#     print("T恤的尺码为{},印到体恤上的字样为{}.".format(cm,zy))
# make_shirt(zy="H",cm="s")

"""8-4 大号 T 恤：修改函数 make_shirt()，使其在默认情况下制作一件印有字样“I love 
Python”的大号 T 恤。调用这个函数来制作如下 T 恤：一件印有默认字样的大号 T 恤、
一件印有默认字样的中号 T 恤和一件印有其他字样的 T 恤（尺码无关紧要）。"""
# def make_shirt(cm="L",zy="I love pyhthon"):
#     print("T恤的尺码为{},印到体恤上的字样为{}.".format(cm, zy))
# make_shirt("中号",)
# make_shirt(zy="我不喜欢c")

"""8-5 城市：编写一个名为 describe_city()的函数，它接受一座城市的名字以及该城
市所属的国家。这个函数应打印一个简单的句子，如 Reykjavik is in Iceland。给用
于存储国家的形参指定默认值。为三座不同的城市调用这个函数，且其中至少有一座城
市不属于默认国家。"""
# def describe_city(name,guojiao="中国"):
#     print("{}是{}的.".format(name,guojiao))
# describe_city("合肥")
# describe_city("纽约","美国")
# describe_city(guojiao="韩国",name="釜山")

"""输出整洁的姓名"""
# def xm(fist_name,last_name):
#     mz = fist_name + last_name
#     return mz
# while True:
#     a = input("输入姓:")
#     if a == "exit":
#         break
#     b = input("输入名字:")
#     if b == "exit":
#         break
#     c = xm(a,b)
#     print(c)

"""把姓名存在字典里"""
# def xm(fist_name,last_name,*zi):
#     ds = {}
#     ds["姓"]=fist_name
#     ds["名"]=last_name
#     ds["字"]=zi
#     return ds
# while True:
#     a = input("输入姓:")
#     if a == "exit":
#         break
#     b = input("输入名字:")
#     if b == "exit":
#         break
#     c = xm(a,b)
#     print(c)

"""8-6 城市名：编写一个名为 city_country()的函数，它接受城市的名称及其所属的
国家。这个函数应返回一个格式类似于下面这样的字符串：
"Santiago, Chile" 
至少使用三个城市国家对调用这个函数，并打印它返回的值。"""
# def city_country(cs,gj):
#     hb = cs+","+gj
#     return hb
# print(city_country("长江","中国"))
# print(city_country("釜山","韩国"))
# print(city_country("耳光","印度"))

"""8-7 专辑：编写一个名为 make_album()的函数，它创建一个描述音乐专辑的字典。
这个函数应接受歌手的名字和专辑名，并返回一个包含这两项信息的字典。使用这个函
数创建三个表示不同专辑的字典，并打印每个返回的值，以核实字典正确地存储了专辑
的信息。
给函数 make_album()添加一个可选形参，以便能够存储专辑包含的歌曲数。如果调
用这个函数时指定了歌曲数，就将这个值添加到表示专辑的字典中。调用这个函数，并
至少在一次调用中指定专辑包含的歌曲数。"""
# def make_album(name,zj,*b):
#     ds = {}
#     ds[name] = str(zj)+str(b)
#     return ds
# a = make_album("罗志祥","多人运动","100场","80个妞","晚上八点")
# b =make_album("周杰伦","莫吉托")
# c =make_album("giao","中国新说唱")
# print(a,b,c,sep="\n")

"""8-8 用户的专辑：在为完成练习 8-7 编写的程序中，编写一个 while 循环，让用户
输入一个专辑的歌手和名称。获取这些信息后，使用它们来调用函数 make_album()，并
将创建的字典打印出来。在这个 while 循环中，务必要提供退出途径。"""
# ds = {}
# def make_album(name,zj,b=""):
#
#     ds[name] = zj+b
#     return ds
# while True:
#     a = input("请输入歌手")
#     if a == "exit":
#         break
#     c = input("请输入专辑")
#     if a == "exit":
#         break
#     b = input("请输入有多少场")
#     if b == "exit":
#         break
#     d=make_album(a,c,b)
# print(d)

"""传递列表"""
# def name(nm):
#     for i in nm:
#         print("你好呀,",i)
# name(["孙悟空","猪八戒","唐僧"])

"""函数中修改列表"""
# def a(x,y):
#     while x:
#         z = x.pop()
#         print("正在打印{}".format(z))
#         y.append(z)
# def b(y):
#     for i in y :
#         print("已打印完:{}".format(i))
#
# x = ["狮子","老虎","索隆","路飞","孙悟空"]
# y =[]
# a(x.copy(),y)
# b(y)
# print(x)

"""8-9 魔术师：创建一个包含魔术师名字的列表，并将其传递给一个名为
show_magicians()的函数，这个函数打印列表中每个魔术师的名字。"""
# def show_magicians(ls):
#     for i in ls:
#         print(i)
# a = ["唐僧","猪八戒","孙悟空","白龙马","沙僧"]
# show_magicians(a)

"""8-10 了不起的魔术师：在你为完成练习 8-9 而编写的程序中，编写一个名为
make_great()的函数，对魔术师列表进行修改，在每个魔术师的名字中都加入字样“the 
Great”。调用函数 show_magicians()，确认魔术师列表确实变了。"""
# def make_great(a,b):
#     while a:
#         c = "伟大的:"+a.pop()
#         b.append(c)
#     return b
# def show_magicians(ls):
#     for i in ls:
#         print(i)
# a = ["唐僧","猪八戒","孙悟空","白龙马","沙僧"]
# b =[]
# make_great(a.copy(),b)
# show_magicians(b)
# print(a)
# print(b)
"""8-11 不变的魔术师：修改你为完成练习 8-10 而编写的程序，在调用函数
make_great()时，向它传递魔术师列表的副本。由于不想修改原始列表，请返回修改后
的列表，并将其存储到另一个列表中。分别使用这两个列表来调用 show_magicians()，
确认一个列表包含的是原来的魔术师名字，而另一个列表包含的是添加了字样“the 
Great”的魔术师名字。"""

"""传递任意参数的实参"""
# def a(*b):
#     print(b)
#     for i in b:
#         print(i)
#
# a(1,2,3,4,5,6)

"""8-12 三明治：编写一个函数，它接受顾客要在三明治中添加的一系列食材。这个
函数只有一个形参（它收集函数调用中提供的所有食材），并打印一条消息，对顾客点
的三明治进行概述。调用这个函数三次，每次都提供不同数量的实参。"""
# def smz(*sc):
#     print("\n你点了以下食材:")
#     for i in sc:
#         print(i)
# smz("炸酱面","方便面",'重庆小面')
# smz("香蕉","牛奶","牛肉")
# smz("粑粑","蛆","苍蝇")

"""8-13 用户简介：复制前面的程序 user_profile.py，在其中调用 build_profile()来
创建有关你的简介；调用这个函数时，指定你的名和姓，以及三个描述你的键值对。"""
# def build_profile(first, last, **user_info):#创建函数 有3个形参
#     profile = {}# 创建一个空字典
#     profile['first_name'] = first #给空字典里添加键值对
#     profile['last_name'] = last #同上
#     for key, value in user_info.items():  #遍历字典
#         profile[key] = value #  给空字典添加键值对
#     return profile # 返回字典
# user_profile = build_profile('孙','悟空',名字="朱浩浩",性别="男",爱好="python")
# print(user_profile)

"""8-14 汽车：编写一个函数，将一辆汽车的信息存储在一个字典中。这个函数总是接
受制造商和型号，还接受任意数量的关键字实参。这样调用这个函数：提供必不可少的
信息，以及两个名称—值对，如颜色和选装配件。这个函数必须能够像下面这样进行调用：
car = make_car('subaru', 'outback', color='blue', tow_package=True) 
打印返回的字典，确认正确地处理了所有的信息。"""
# def car_name(manufacturer,model,**user_info):
#     car_message = {}
#     car_message["manufacturer_name"] =manufacturer
#     car_message["model_name"] =model
#     for key,value in user_info.items():
#         car_message[key] = value
#     return car_message
# car = car_name('subaru', 'outback', color='blue', tow_package=True)
# print(car)

"""8-15 打印模型：将示例 print_models.py 中的函数放在另一个名为 printing_ 
functions.py 的文件中；在 print_models.py 的开头编写一条 import 语句，并修改这个文
件以使用导入的函数。"""