#网络爬虫1.0
import requests
r=requests.get(input("输入网址:"))
print("连接:{}".format(r.status_code))
type=(r)
