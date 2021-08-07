#工作日努力达到多少才能和每天都努力一样
dayfactor=0.01#定义进步值为dayfactor
def dayup(dayfactor):
    dayup = 1  # 初始值为1

    for i in range(365):
        if i%7 in [6,0]:
            dayup*=(1-0.01)
        else:
            dayup*=(1+dayfactor)
    return dayup
while dayup(dayfactor)<37.8:
    dayfactor+=0.01
print("工作日努力达到{}和每天努力一样".format(dayfactor))
