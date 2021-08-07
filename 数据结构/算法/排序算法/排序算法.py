import  random
def random_number():
    """随机生成一百个数"""
    ls = []
    for i in range(100):
        a = random.randint(0,100)
        ls.append(a)
    print("需要排序的数列为：",ls)
    return ls

def sort(ls):
    """进行排序
    ls ： 传入需要排序的列表
    """
    ls_a = []
    for i in range(len(ls)):
        k = min(ls)
        ls_a.append(k)
        ls.remove(k)
    print("排序后的数列为：",end=" ")
    for j in ls_a:
        print(j,end=" ")
    return ls_a
if __name__ == '__main__':
    a = random_number()
    sort(a)