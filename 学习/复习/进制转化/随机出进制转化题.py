# 随机出 进制转化题目
import random


def conversion(a, b):
    """

    :param a: a为题目总数
    :return: b为数值的长度
    """
    i = 0
    ls_num = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "A", "B", "C", "D", "E", "F"]
    ls_conversion = ["B", "H", "O", "D"]
    while i < a:
        ls_a = ""
        num_a = random.choice(ls_conversion)
        num_b = random.choice(ls_conversion)
        if num_a == num_b:
            continue
        if num_a == "B":
            for x in range(b):
                num_c = random.choice(ls_num[:2])
                ls_a += num_c
            print("{}({})= ? ({})".format(ls_a, num_a, num_b))
        elif num_a == "H":
            for x in range(b):
                num_c = random.choice(ls_num[:])
                ls_a += num_c
            print("{}({})= ? ({})".format(ls_a, num_a, num_b))
        elif num_a == "D":
            for x in range(b):
                num_c = random.choice(ls_num[:10])
                ls_a += num_c
            print("{} ({})= ? ({})".format(ls_a, num_a, num_b))
        elif num_a == "O":
            for x in range(b):
                num_c = random.choice(ls_num[:8])
                ls_a += num_c
            print("{}({})= ? ({})".format(ls_a, num_a, num_b))
        i += 1


conversion(10, 3)
