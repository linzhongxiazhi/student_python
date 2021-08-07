import os


def judge(a, b):
    x = get(a)
    y = get(b)
    if x == y:
        return True
    return False


def get(num):
    n = []
    while num > 10:
        n.append(num % 10)
        num = int(num / 10)
    n.append(num)
    n.sort()
    return n


if __name__ == '__main__':
    l = [123, 213, 132, 156, 403, 314]
    flag = [-1 for _ in l]
    for i in range(0, len(l) - 1):
        for j in range(i + 1, len(l)):
            if flag[i] == -1:
                if judge(l[i], l[j]):
                    flag[j] = i
    result = []
    for i, f in enumerate(flag):
        if f == -1:
            result.append(l[i])
    print(result)

