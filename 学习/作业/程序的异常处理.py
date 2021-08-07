#帅不帅2.0
try:
    print("你说浩哥帅不帅")
    while True:
        num1=input("请回答帅与不帅:")
        if "不" in num1:
            print("再给你一次机会:")
            continue
        if "丑"in num1:
            print("再给你一次机会")

        else:
            print("同帅,同帅")
            break
except SyntaxError:
    print("解析错误:")
else:
    print("没有出错")
finally:
    print("程序运行完毕")