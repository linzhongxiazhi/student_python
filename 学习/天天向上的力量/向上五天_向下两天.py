#向上五天向下两天
import math
dayup=1
for i in range(365):
    if i % 7 in [6,0]:
        dayup=dayup*(1-0.01)
    else:
        dayup=dayup*(1+0.01)
print("向上五天向下两天：{}".format(dayup))
