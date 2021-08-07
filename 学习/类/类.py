# class dog():
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age
#     def dun(self):
#         print(self.name+"蹲下了")
#     def tiao(self):
#         print(self.name+"跳起来了")
#
# my_dog=dog("小白",4)
# my_dog.tiao()
# my_dog.dun()
# print(my_dog.name)
# print(my_dog.age)
# print("我的小狗叫{},今年{}岁了.".format(my_dog.name,my_dog.age))

"""9-1 餐餐馆馆 ：创建一个名为Restaurant 的类，其方法__init__() 设置两个属性：restaurant_name 和cuisine_type 。
创建一个名 为describe_restaurant() 的方法和一个名为open_restaurant() 的方法，其中前者打印前述两项信息，而后者打印一条消息，指出餐馆正在营业。"""


# class Restaurant():
#
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.resturant_name =restaurant_name
#         self.cuisine_type = cuisine_type
#
#     def describe_restaurant(self):
#         print(self.restaurant_name)
#         print(self.cuisine_type)
#
#     def open_restaurant(self):
#         print(self.restaurant_name + "正在营业")
#
#
# a = Restaurant("三和饭店", "中餐")
# a.describe_restaurant()
# a.open_restaurant()


# """9-3 用用户户 ：创建一个名为User 的类，其中包含属性first_name 和last_name ，还有用户简介通常会存储的其他几个属性。在类User
# 中定义一个名 为describe_user() 的方法，它打印用户信息摘要；再定义一个名为greet_user() 的方法，它向用户发出个性化的问候。"""
# class User():
#     def __init__(self,first_name,last_name):
#         self.first_name = first_name
#         self.last_name = last_name
#     def describe_user(self):
#         print(self.first_name)
#         print(self.last_name)
#     def greet_user(self):
#         print(self.first_name+self.last_name+"欢迎登录!")
# a = User("朱","浩浩")
# a.describe_user()
# a.greet_user()


"""9-4 就就餐餐人人数数 ：在为完成练习9-1而编写的程序中，添加一个名为number_served 的属性，并将其默认值设置为0。根据这个类创建一个名为restaurant 的实 
例；打印有多少人在这家餐馆就餐过，然后修改这个值并再次打印它。添加一个名为set_number_served() 的方法，它让你能够设置就餐人数。调用这个方法并向它传递一个值
，然后再次打印这个值。 添加一个名为increment_number_served() 的方法，它让你能够将就餐人数递增。调用这个方法并向它传递一个这样的值：你认为这家餐馆每天可能接待的就 餐人数。"""
# class Restaurant():
#
#
#     def __init__(self, restaurant_name, cuisine_type):
#         self.restaurant_name = restaurant_name
#         self.cuisine_type = cuisine_type
#         self.number_served = 0 # 设定默认值
#
#     def describe_restaurant(self):
#         print(self.restaurant_name)
#         print(self.cuisine_type)
#
#     def open_restaurant(self):
#         print(self.restaurant_name + "正在营业")
#     def set_number_served(self,number_served): #修改默认值
#         self.number_served = number_served
#     def increment_number_served(self,number_served): #增加默认值
#         self.number_served += number_served
# # a = Restaurant("三和饭店", "中餐")
# # a.describe_restaurant()
# # a.open_restaurant()
#
# restaurant = Restaurant("三和饭店","中餐")
# print("现在三和饭店的人数:",restaurant.number_served)
# restaurant.number_served =110
# print("三和饭店的人数为:",restaurant.number_served)
# restaurant.set_number_served(100)
# print("三和饭店的人数为:",restaurant.number_served)
# restaurant.increment_number_served(100)
# print("三和饭店的人数为:",restaurant.number_served)

"""继承"""
"""9-6 冰淇淋小店：冰淇淋小店是一种特殊的餐馆。编写一个名为 IceCreamStand 的
类，让它继承你为完成练习 9-1 或练习 9-4 而编写的 Restaurant 类。这两个版本的
Restaurant 类都可以，挑选你更喜欢的那个即可。添加一个名为 flavors 的属性，用于
存储一个由各种口味的冰淇淋组成的列表。编写一个显示这些冰淇淋的方法。创建一个
IceCreamStand 实例，并调用这个方法。"""
class Restaurant():


    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0 # 设定默认值

    def describe_restaurant(self):
        print(self.restaurant_name)
        print(self.cuisine_type)

    def open_restaurant(self):
        print(self.restaurant_name + "正在营业")
    def set_number_served(self,number_served): #修改默认值
        self.number_served = number_served
    def increment_number_served(self,number_served): #增加默认值
        self.number_served += number_served

class IceCteamStand(Restaurant):
    def __init__(self,testaurant_name,cuisine_type):
        super().__init(testaurant_name,cuisine_type)
    def flavors(self,):
