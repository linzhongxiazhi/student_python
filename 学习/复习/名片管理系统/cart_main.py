# 导入扩展包
import cart_tools

# 主程序
while True:
    # 显示菜单界面
    cart_tools.show_menu()
    # 获得用户输入操作
    a_str = input("请输入要查询的操作:")

    # 根据用户输入反馈
    if a_str in ["1", "2", "3"]:
        # 当用户输入123时候的反馈
        if a_str == "1":
            cart_tools.new_card()
        elif a_str == "2":
            cart_tools.show_all()
        else:
            cart_tools.search_card()

    elif a_str in ["0"]:
        # 用户退出
        print("程序结束欢迎再次使用!")
        break

    else:
        # 用户输入错误时候的反馈
        print("输入由误,请重新输入!")
