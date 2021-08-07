# 每天得多努力
dayup = 1
daya = 37.5


def dayupb(dfx):
    dayup = 1
    for i in range(365):
        if i % 7 in [0, 6]:
            dayup = dayup - dayup * 0.01
        else:
            dayup = dayup + dayup * dfx
    return dayup


dayx = 0.01
while dayupb(dayx) < daya:
    dayx += 0.001
print("工作日的时候的努力参数是：{:.3f}".format(dayx))
