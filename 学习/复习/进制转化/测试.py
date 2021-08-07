import random

ls_num = ["H", "O", "B", "D"]
extent = ["100", "1000", "10000", "100000", "1000000", "10000000", "100000000", "1000000000", "10000000000",
          "100000000000"]


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
        num_a = str(random.randint(int(extent[c - 2], int(extent[c - 1]))))
        if a == "2":
            print("{} (D) = ? (B)".format(num_a))
        elif a == "8":
            print("{} (D) = ? (0)".format(num_a))
        elif a == "16":
            print("{} (D) = ? (H)".format(num_a))
        elif a == "0":
            print("{} (D) = ? ({})".format(num_a, random.choice(ls_num)))
        i += 1


ten("8", 10, 1)
