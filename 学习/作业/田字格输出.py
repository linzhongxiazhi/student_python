#e5.1函数化输出田字格
def tianzige(h,l):
    a,b,c,d = "＋","－","丨","  "
    hang = 4*b + a
    ch  = 4*d + c
    for i in range(h):
        print(a+hang*l)
        print(c + ch*l)
        print(c + ch*l)
        print(c + ch*l)
        print(c + ch*l)
    print(a+hang*l)

h,l = eval(input("请输入行和列(用逗号隔开)："))
tianzige(h,l)
