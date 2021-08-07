def fun(n,x,y,z):
    if n==1:
        print(x,"--->",z)
    else:
        fun(n-1,x,z,y)
        print(x,"--->",z)
        fun(n-1,y,x,z)
a=int(input("输入有几个盘子："))
print(fun(a,"塔1","塔2","塔3"))
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        
