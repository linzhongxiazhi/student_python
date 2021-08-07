import requests
# url="https://item.jd.com/100018970138.html"
#
# try:
#     r = requests.get(url)
#     r.raise_for_status()
#     r.encoding=r.apparent_encoding
#     print(r.text[:1000])
# except:
#     print("爬取失败")

url ="https://gimg2.baidu.com/image_search/src=http%3A%2F%2Fcar0.autoimg.cn%2Fupload%2F2012%2F11%2F1%2Fv_201211011828160453655.jpg&refer=http%3A%2F%2Fcar0.autoimg.cn&app=2002&size=f9999,10000&q=a80&n=0&g=0n&fmt=jpeg?sec=1627133617&t=f6b197e3f9406f0c59de2e5a5dcc1e53"
try:
    kv = {"user-agent":"Mozilla/5.0"}
    r=requests.get(url,headers=kv)
    r.raise_for_status()
    r.encoding=r.apparent_encoding
    print(r.text[:1000])
    print(r.request.headers)
except:
    print("爬取失败")