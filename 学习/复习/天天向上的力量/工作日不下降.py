# 工作日不下降
dayup = 1
dayfactor = 0.01
for i in range(365):
    if i % 7 in [6, 0]:
        pass
    else:
        dayup = dayup + dayup * dayfactor
print("工作日不下降365天后为：{:.2f}".format(dayup))
