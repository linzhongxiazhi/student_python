#中文凯撒密码
n = input("请输入明文:")
for i in n:
    if 0x4e00<=ord(i)<=0x9fa5:
        print(chr(0x4e00+(ord(i)-0x4e00+10451)%20902),end="")
    else:
        print(i,end="")

