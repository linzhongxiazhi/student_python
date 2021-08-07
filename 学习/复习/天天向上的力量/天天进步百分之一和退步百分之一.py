# 天天进步百分之一和退步百分之一
dayup = (1 + 0.01) ** 365
daydown = (1 - 0.01) ** 365
print("进步365天后为：{:.2f}，退步365天后为：{:.2f}".format(dayup, daydown))
