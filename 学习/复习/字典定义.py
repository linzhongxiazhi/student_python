# 字典定义
zhuhaohao = {
    "名字": "朱浩浩",
    "QQ": 1134393383,
    "身高": "16cm",
    "体重": "50kg",
}
print(zhuhaohao)
print(zhuhaohao.keys())
print(zhuhaohao.values())
print(zhuhaohao.items())
# 增
print("增")
zhuhaohao["年龄"] = 21
zhuhaohao["年龄2"] = 21
print(zhuhaohao, "\n")
# 删
print("删除")
zhuhaohao.pop("年龄2")
print(zhuhaohao, "\n")
# 改
print("修改")
zhuhaohao["年龄"] = "20"
print(zhuhaohao, "\n")
# 查
print("查找")
print(zhuhaohao)

print("---" * 50)
for i, y in zhuhaohao.items():
    print(i)
    print(y)
