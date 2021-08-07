# 爬虫初体验
import requests
print("访问一个网站")
r = requests.get("http://www.baidu.com")
print(r.status_code,"#200表示连接成功")
print(r.encoding )  # 更改网页为utf - 8编码
print(r.apparent_encoding)
print("将对象转化为utf-8编码并打印出来")
r.encoding = "utf-8"
print(r.text)



