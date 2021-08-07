import random

ls_num = ["H", "B", "O", "D"]
extent = ["100", "1000", "10000", "100000", "1000000", "10000000", "100000000", "1000000000", "10000000000",
          "100000000000"]


# 显示菜单
def show():
    while True:
        print("2-二进制，8-八进制，10-十进制，16-十六进制，0-随机")
        num_a = input("你想做什么进制转化题:")
        num_b = input("你想做{}进制转化为什么进制题目:".format(num_a))
        num_c = eval(input("你想做什么难度的题目？1-10难度："))
        if num_a and num_b not in ["2", "8", "10", "16", "0"]:
            print("您的输入有误，请重新输入")
            continue
        else:
            break
    return num_a, num_b, num_c


# 二进制
def two(a, b, c):
    """

    :param a: a是要转化的进制
    :param b: b是要转化的题目的数量
    :param c: c是题目难度
    :return:
    """
    i = 0
    ls_num.remove("B")
    while i < int(b):
        num_a = str(bin(random.randint(1, int(extent[c - 1]))))
        if a == "8":
            print("{} (B) = ? (O)".format(num_a[2:]))
        elif a == "10":
            print("{} (B) = ? (D)".format(num_a[2:]))
        elif a == "16":
            print("{} (B) = ? (H)".format(num_a[2:]))
        elif a == "0":
            print("{} (B) = ? ({})".format(num_a[2:], random.choice(ls_num)))

        i += 1


# 八进制
def eight(a, b, c):
    """

    :param a: a是要转化的进制
    :param b: b是要转化的题目的数量
    :param c: c是题目难度
    :return:
    """
    i = 0
    ls_num.remove("O")
    while i < int(b):
        num_a = str(oct(random.randint(1, int(extent[c - 1]))))
        if a == "2":
            print("{} (O) = ? (B)".format(num_a[2:]))
        elif a == "10":
            print("{} (O) = ? (D)".format(num_a[2:]))
        elif a == "16":
            print("{} (O) = ? (H)".format(num_a[2:]))
        elif a == "0":
            print("{} (O) = ? ({})".format(num_a[2:], random.choice(ls_num)))

        i += 1


# 十进制
def ten(a, b, c):
    """

    :param a: a是要转化的进制
    :param b: b是要转化的题目的数量
    :param c: c是题目难度
    :return:
    """
    i = 0
    ls_num.remove("D")
    while i < int(b):
        num_a = str(random.randint(1, int(extent[c - 1])))
        if a == "2":
            print("{} (D) = ? (B)".format(num_a))
        elif a == "8":
            print("{} (D) = ? (0)".format(num_a))
        elif a == "16":
            print("{} (D) = ? (H)".format(num_a))
        elif a == "0":
            print("{} (D) = ? ({})".format(num_a, random.choice(ls_num)))
        i += 1


# 十六进制
def sixteen(a, b, c):
    """

    :param a: a是要转化的进制
    :param b: b是要转化的题目的数量
    :param c: c是题目难度
    :return:
    """
    i = 0
    ls_num.remove("H")
    while i < int(b):
        num_a = str(hex(random.randint(1, int(extent[c - 1]))))
        if a == "2":
            print("{} (H) = ? (B)".format(num_a[2:]))
        elif a == "10":
            print("{} (H) = ? (D)".format(num_a[2:]))
        elif a == "8":
            print("{} (H) = ? (0)".format(num_a[2:]))
        elif a == "0":
            print("{} (H) = ? ({})".format(num_a[2:], random.choice(ls_num)))

        i += 1


# 随机：
def rdm(b, c):
    """

    :param b: 要写的题目
    :param c: 题目难度
    :return:
    """
    ls_A_a = ["B", "O", "D", "H"]
    i = 0
    while i < b:
        ls_A_B = random.randint(0, 3)
        if ls_A_a[ls_A_B] == "B":
            ls_B_a = ["O", "D", "H"]
            num_a = str(bin(random.randint(1, int(extent[c - 1]))))
            print("{} (B) = ? ({})".format(num_a[2:], random.choice(ls_B_a)))
        elif ls_A_a[ls_A_B] == "O":
            ls_B_a = ["B", "D", "H"]
            num_a = str(oct(random.randint(1, int(extent[c - 1]))))
            print("{} (O) = ? ({})".format(num_a[2:], random.choice(ls_B_a)))
        elif ls_A_a[ls_A_B] == "D":
            ls_B_a = ["B", "O", "H"]
            num_a = str(int(random.randint(1, int(extent[c - 1]))))
            print("{} (D) = ? ({})".format(num_a[2:], random.choice(ls_B_a)))
        elif ls_A_a[ls_A_B] == "H":
            ls_B_a = ["B", "D", "O"]
            num_a = str(hex(random.randint(1, int(extent[c - 1]))))
            print("{} (H) = ? ({})".format(num_a[2:], random.choice(ls_B_a)))
        i += 1
