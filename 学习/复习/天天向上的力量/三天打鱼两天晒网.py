# 三天打鱼两天晒网
def dayup(df):
    dayup = 1
    for i in range(365):
        if i % 5 in [0, 4]:
            dayup = dayup - dayup * df
        else:
            dayup = dayup + dayup * df
    return dayup


a = dayup(0.01)
print("三天打鱼两天晒网一年后：{:.2f}".format(a))
