print("凯撒密码加密")
a1= input("请输入明文:")
for i in a1:
    if ord("a") <= ord(i) <= ord("z"):
        print("{}".format(chr(ord("a")+(ord(i)+3-ord("a")) % 26)), end="")
    else:
        print("{}".format(i), end="")

