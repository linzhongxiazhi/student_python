#爬虫
from requests import *
r = get("http://zhongguose.com/#chahuahong")
print(r.status_code)
print(r.encoding)
r.encoding="utf-8"
print(r.text)
print(r.encoding)