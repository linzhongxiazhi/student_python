card_list = []


def show_menu():
    """ 显示菜单
    """
    print("-" * 50)
    print("")
    print("1.新建名片")
    print("2.显示全部")
    print("3.查询名片")
    print("")
    print("0.退出系统")
    print("")
    print("-" * 50)


def new_card():
    """新建卡片
    """
    print("-" * 50)
    print("功能:新建名片")

    # 获得用户输入
    name = input("请输入名字:")
    qq = input("请输入QQ:")
    email = input("请输入邮箱:")
    phone = input("请输入电话:")

    # 将输入的信息放入字典
    card_dict = {}
    card_dict["name"] = name
    card_dict["QQ"] = qq
    card_dict["email"] = email
    card_dict["phone"] = phone

    # 将字典添加进列表
    card_list.append(card_dict)

    # 打印一遍列表
    print(card_list)


def show_all():
    """显示全部
    """
    print("-" * 50)
    print("功能:显示全部")
    # 判断列表又没有存储名片
    if len(card_list) == 0:
        print("还没有存储任何名片")
        return
    # 遍历列表打印字典
    for i in ["姓名", "电话", "邮箱", "QQ"]:
        print(i, end="\t\t")
    print("")
    print("=" * 50)
    for card_dict in card_list:
        print("{}{}{}{}{}{}{}".format(card_dict["name"], "\t\t", card_dict["phone"], "\t\t", card_dict["email"], "\t\t",
                                      card_dict["QQ"]))


def search_card():
    """搜索名片
    """
    print("-" * 50)
    print("功能:搜索名片")

    find_name = input("请输入要搜索的姓名:")
    for card_dict in card_list:
        if card_dict["name"] == find_name:
            for i in ["姓名", "电话", "邮箱", "QQ"]:
                print(i, end="\t\t")
            print("")
            print("=" * 50)
            print("{}{}{}{}{}{}{}".format(card_dict["name"], "\t\t", card_dict["phone"], "\t\t", card_dict["email"],
                                          "\t\t", card_dict["QQ"]))
            print("-" * 50)
            # 修改字典
            a_str = input("请选择要对名片进行的操作:"
                          "[1] 修改名片"
                          "[2] 删除名片"
                          "[0] 返回上级菜单:")
            if a_str == "1":
                card_dict["name"] = xiugai(card_dict["name"], "请输入名字:")
                card_dict["phone"] = xiugai(card_dict["phone"], "请输入电话:")
                card_dict["QQ"] = xiugai(card_dict["QQ"], "请输入QQ:")
                card_dict["email"] = xiugai(card_dict["email"], "请输入邮件:")
                print("修改成功")
            elif a_str == "2":
                card_list.remove(card_dict)
                print("删除成功")
            break
    else:
        print("没有找到")


def xiugai(zidian, tisi):
    """修改名片
    """
    # 1.提示用户输入内容
    b_str = input(tisi)
    # 2.对用户的输入进行判断,如果输入了内容返回用户输入的
    if len(b_str) > 0:
        return b_str
    # 3.如果用户没有输入内容,返回原来的值
    else:
        return zidian
