# 工作三天休息一天
dayup = 1
dayfactor = 0.01
for i in range(365):
    if i % 4 in [0]:
        dayup = dayup - dayup * dayfactor
    else:
        dayup = dayup + dayup * dayfactor
print("工作三天休息一天365天后为：{:.2f}".format(dayup))
