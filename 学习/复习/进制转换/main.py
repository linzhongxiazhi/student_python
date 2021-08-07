import toll

str_a = toll.show()
count_a = eval(input("您要写多少题？："))
"""二进制"""
if str_a[0] == "2":
    if str_a[1] == "2":
        print("2进制无需转化成2进制的呢")

    else:
        toll.two(str_a[1], count_a, str_a[2])

"""八进制"""
if str_a[0] == "8":
    if str_a[1] == "8":
        print("8进制无需转化成8进制的呢")
    else:
        toll.eight(str_a[1], count_a, str_a[2])

"""十进制"""
if str_a[0] == "10":
    if str_a[1] == "10":
        print("10进制无需转化成10进制的呢")
    else:
        toll.ten(str_a[1], count_a, str_a[2])

"""十六进制"""
if str_a[0] == "16":
    if str_a[1] == "16":
        print("16进制无需转化成16进制的呢")
    else:
        toll.sixteen(str_a[1], count_a, str_a[2])

"""随机"""
if str_a[0] == "0":
    toll.rdm(count_a, str_a[2])
