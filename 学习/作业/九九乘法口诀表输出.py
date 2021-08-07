#乘法口诀表输出
def muTable():
    for i in range(1,100):
        for n in range(1,i+1):
            print("{}x{}={}".format(n,i,i*n),end="        ")
        print()
muTable()