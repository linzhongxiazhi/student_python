# 工作人进步周末退步365天后
dayup = 1
dayx = 0.01
for i in range(365):
    if i % 7 in [0, 6]:
        dayup = dayup - dayx * dayup
    else:
        dayup = dayup + dayx * dayup
print("365天后为：{:.2f}".format(dayup))
