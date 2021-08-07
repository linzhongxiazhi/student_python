import random

extent = ["100", "1000", "10000", "100000", "1000000", "10000000", "100000000", "1000000000", "10000000000",
          "100000000000"]


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


rdm(10, 10)
