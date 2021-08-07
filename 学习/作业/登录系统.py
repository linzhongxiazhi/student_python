#简易登录系统
num1 ="1134393383"
num2= "zhu006622","123"
while True:
    num3=input("请输入用户名:")
    if num3==num1:
        print("用户名正确")
        while True:
            num4=input("请输入密码:")
            if num4==num2:
                print("登录成功")
                break
            else:
                print("用户输入错误,请重新输入")
        break
    else:
        print("用户名输入错误,请重新输入:")
