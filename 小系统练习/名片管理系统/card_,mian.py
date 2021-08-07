import card_tools

# 程序启动界面
card_tools.show_menu()
while True:
    # 用户根据数字选择不同的功能
    a = input("请输入你选择的功能:")

    if a in ["1","2","3"]:
        #根据用户选择的功能,执行不同的功能
        if a == "1":
            card_tools.new_card()
        elif a == "2":
            card_tools.show_all()
        else:
            card_tools.search_card()

    elif a == "0":
        print("程序已退出运行")
        break

    else:
        print("您的输入有误请重新输入")
        continue
