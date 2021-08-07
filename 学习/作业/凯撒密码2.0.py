print("凯撒密码")
try:
    a= eval(input("加密(1),解密(2):"))
    if a in [1,2]:
        if a in [1]:
            a1=input("请输入明文:")
            for i in a1:
                if ord("a")<=ord(i)<=ord("z"):
                    print("{}".format(chr(ord("a")+(ord(i)-ord("a")+3)%26)),end='')
                elif ord("A")<=ord(i)<=ord("Z"):
                    print("{}".format(chr(ord("A") + (ord(i) - ord("A") + 3) % 26)), end='')
                else:
                    print("{}".format(i),end="")
        if a in [2]:
            a1=input("请输入明文:")
            for i in a1:
                if ord("a") <= ord(i) <= ord("z"):
                    print("{}".format(chr(ord("a") + (ord(i) - ord("a") -3) % 26)), end='')
                elif ord("A")<=ord(i)<=ord("Z"):
                    print("{}".format(chr(ord("A") + (ord(i) - ord("A") - 3) % 26)), end='')
                else:
                    print("{}".format(i), end="")
    else:
        print("请选择加密或解密")
except :
    print("请输入数字1或2")