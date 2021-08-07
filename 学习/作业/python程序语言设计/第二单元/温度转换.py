温度 = input("请输入温度:")
if 温度[-1] in ["c","C"]:
    f = eval(温度[0:-1])*1.8+32
    print("转化后的温度为{:.2f}f".format(f))
if 温度[-1] in ["f","F"]:
    c = (eval(温度[0:-1])-32)/1.8
    print("转化后的温度为{:.2f}c".format(c))
