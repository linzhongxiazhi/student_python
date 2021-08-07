def show_menu():
    """显示菜单
    """
    print("*" * 50)
    print("欢迎使用[名片管理系统] v1.0")
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("*" * 50)

def new_card():
    """新建名片
    """
    global card_list
    card_list = []

    print("-"*50)
    print("功能:新建名片")
    name =input("请输入姓名:")
    qq = input("请输入QQ:")
    phone = input("请输入电话:")
    email = input("请输入邮箱:")
    #将信息保持到字典
    card_dict={"名字":name,
               "电话":phone,
               "QQ":qq,
               "邮箱":email,}
    card_list.append(card_dict)
    print(card_list)
    print("成功添加{}的名片".format(card_dict["名字"]))
    #在pycharm中可以使用shift+F6统一修改变量名

def show_all():
    """显示全部
    """
    print("-"*50)
    print("功能:显示全部")
    for i in card_list():
        print(i)

def search_card():
    """搜索名片
    """
    print("-"*50)
    print("功能:搜索名片")
