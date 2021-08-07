# 一个长方体,如果长增加3厘米,就变成一个正方体,表面积增加144平方厘米,长方体的表面积和体积是多少?
import sympy

x, h = sympy.symbols("x h")
a = sympy.solve([x - h - 3, 2 * x ** 2 + 4 * x * h + 144 - 2 * x ** 2 - 4 * x * (h + 3)], [x, h])
print("这个长方体的长为:{},宽为:{}".format(a[x], a[h]))
v = (a[x] ** 2) * a[h]
s = 2 * a[x] ** 2 + 4 * a[x] * a[h]
print("这个长方体的体积是:{}".format(v))
print("这个长方体的表面积是:{}".format(s))
