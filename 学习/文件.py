# 导入包
import random, time, os

# 清屏(跨平台的哦, 滑稽)
def clear_screen():
    # 不要学我这么写，我是为了省事
    if os.sep == '/':
        os.system('clear')
    else:
        os.system('cls')

# 模拟延时效果
def delay_waiting(content, frequency):
    print('%s.' % content, end='', flush=True)
    for x in range(1, frequency):
       time.sleep(1)
       print('.', end='', flush=True)
    time.sleep(1)
    print(' succeeded.')

# 模拟登陆锡安主机
def login_zion():
    clear_screen()
    delay_waiting('connecting to Zion host', 2)
    time.sleep(0.5)
    print('enter username: Neo')
    time.sleep(0.2)
    print('enter password: ******')
    time.sleep(0.2)
    delay_waiting('logging in.', 2)
    time.sleep(0.7)
    clear_screen()
    print('Hello, Neo.')
    time.sleep(1)

# 模拟登陆锡安主机
login_zion()
# 清屏
clear_screen()
# 创建一个包含了a-z,A-Z,0-9的字符集
charts = [*[chr(x) for x in range(65, 123) if x not in range(91, 97)], *map(str, range(10))]
# 死循环
while True:
    # 每次打印延时0.009秒
    time.sleep(0.012)
    # 我屏幕的最大字符数量是158
    # 这里的79是为了显示的时候每个字符间会有一个空格，然后正好占满158个字符(78个字符 + 78个空格 + 1个字符)
    # 或者你也可以写成:
    #     print((' ' * 3).join(random.choices(charts, k=40)))
    print(*random.choices(charts, k=79))