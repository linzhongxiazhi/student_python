import requests
import json
import time

num = 454
rangeSet = num + 1
cookies = {'MOD_AUTH_CAS': 'YcxNA903马赛克583063221'}

global null
null=''
headers = \
    {
        "Host": "hnu马赛克y.com",
        "Connection": "close",
        "Content-Length": "3596",
        "Accept": "application/json, text/plain, */*",
        "Origin": "https:马赛克pd马赛克om",
        "X-Requested-With": "XMLHttpRequest",
        "User-Agent": "Mozilla/5.0 (Linux; Android 10; Redmi K20 Pro Build/QKQ1.190825.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/77.0.3865.92 Mobile Safari/537.36 yiban/8.1.9 cpdaily/8.1.9 wisedu/8.1.9",
        "Sec-Fetch-Mode": "cors",
        "Content-Type": "application/json",
        "Sec-Fetch-Site": "same-origin",
        "Referer": "https://hnua马赛克wec-coun马赛克llector-马赛克x.html?collectorWid=422",
        "Accept-Encoding": "gzip,deflate",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7"
    }

while num<rangeSet:
    body = {"formWid": "194", "collectWid": "422", "schoolTaskWid": "17174", "form": [
        {"wid": "1004", "formWid": "194", "fieldType": 2, "title": "你所在的校区",
         "description": "如果你所在的学校只有一个校区，请选择【本校区】；如果有多个校区的，请选择【其他】，并填写校区名称", "minLength": 0, "sort": "1",
         "maxLength": null, "isRequired": 1, "imageCount": null, "hasOtherItems": 1, "colName": "field001",
         "value": "其他", "fieldItems": [
            {"itemWid": "4035", "content": "其他", "isOtherItems": 1, "contendExtend": "马赛克校区", "isSelected": 1}]},
        {"wid": "1005", "formWid": "194", "fieldType": 1, "title": "你的身份证号", "description": "请填入完整18位身份证号",
         "minLength": 18, "sort": "2", "maxLength": 18, "isRequired": 1, "imageCount": null, "hasOtherItems": 0,
         "colName": "field002", "value": "4128012001马赛克0", "fieldItems": []},
        {"wid": "1006", "formWid": "194", "fieldType": 1, "title": "你的当前所在地区",
         "description": "请选择你目前所在的省、市、区（县），不在大陆地区的，请选择海外具体地区。", "minLength": 1, "sort": "3", "maxLength": 300,
         "isRequired": 1, "imageCount": -2, "hasOtherItems": 0, "colName": "field003", "value": "马赛克省/马赛克市/马赛克区",
         "fieldItems": [], "area1": "马赛克省", "area2": "马赛克市", "area3": "马赛克区"},
        {"wid": "1007", "formWid": "194", "fieldType": 2, "title": "你所在的小区（村）是否有确诊情况？", "description": "",
         "minLength": 0, "sort": "4", "maxLength": null, "isRequired": 1, "imageCount": null, "hasOtherItems": 0,
         "colName": "field004", "value": "否",
         "fieldItems": [{"itemWid": "4037", "content": "否", "isOtherItems": 0, "contendExtend": "", "isSelected": 1}]},
        {"wid": "1008", "formWid": "194", "fieldType": 2, "title": "共同居住人是否有确诊病例？", "description": "", "minLength": 0,
         "sort": "5", "maxLength": null, "isRequired": 1, "imageCount": null, "hasOtherItems": 0, "colName": "field005",
         "value": "否",
         "fieldItems": [{"itemWid": "4039", "content": "否", "isOtherItems": 0, "contendExtend": "", "isSelected": 1}]},
        {"wid": "1009", "formWid": "194", "fieldType": 2, "title": "是否去过湖北疫区？", "description": "", "minLength": 0,
         "sort": "6", "maxLength": null, "isRequired": 1, "imageCount": null, "hasOtherItems": 0, "colName": "field006",
         "value": "否",
         "fieldItems": [{"itemWid": "4041", "content": "否", "isOtherItems": 0, "contendExtend": "", "isSelected": 1}]},
        {"wid": "1010", "formWid": "194", "fieldType": 2, "title": "与疫区人员是否有接触？", "description": "", "minLength": 0,
         "sort": "7", "maxLength": null, "isRequired": 1, "imageCount": null, "hasOtherItems": 0, "colName": "field007",
         "value": "否",
         "fieldItems": [{"itemWid": "4043", "content": "否", "isOtherItems": 0, "contendExtend": "", "isSelected": 1}]},
        {"wid": "1011", "formWid": "194", "fieldType": 2, "title": "是否留置观察？", "description": "", "minLength": 0,
         "sort": "8", "maxLength": null, "isRequired": 1, "imageCount": null, "hasOtherItems": 0, "colName": "field008",
         "value": "否",
         "fieldItems": [{"itemWid": "4045", "content": "否", "isOtherItems": 0, "contendExtend": "", "isSelected": 1}]},
        {"wid": "1012", "formWid": "194", "fieldType": 2, "title": "是否曾经确诊？", "description": "", "minLength": 0,
         "sort": "9", "maxLength": null, "isRequired": 1, "imageCount": null, "hasOtherItems": 0, "colName": "field009",
         "value": "否",
         "fieldItems": [{"itemWid": "4047", "content": "否", "isOtherItems": 0, "contendExtend": "", "isSelected": 1}]},
        {"wid": "1013", "formWid": "194", "fieldType": 2, "title": "健康状况是否良好？", "description": "", "minLength": 0,
         "sort": "10", "maxLength": null, "isRequired": 1, "imageCount": null, "hasOtherItems": 0,
         "colName": "field010", "value": "是",
         "fieldItems": [{"itemWid": "4048", "content": "是", "isOtherItems": 0, "contendExtend": "", "isSelected": 1}]}]}
    body["collectWid"] = num
    body1 = json.dumps(body)
    r = requests.post("https://hnu马赛克com/wec-coun马赛克lector-apps/stu/co马赛克or/sub马赛克m",
                      headers=headers, data=body1, cookies=cookies)

    check = r.text.split("\",\"")[1].split("\"")[2]
    checkNO1 = "该收集已结束！"
    checkNO2 = "您无需填写该信息收集，请勿代填"
    checkNO3 = "数据异常，该收集不存在，请联系管理员！"
    checkYES = "SUCCESS"
    if check == checkNO2:
     print("不是本班,自动忽略，一分钟后程序将判断编号：",num)
     time.sleep(60)
    else:
        pass

    if check == checkNO1:
        print("该次收集已结束,无法提交，程序将判断编号：",num)
    else:
        pass

    if check == checkNO3:
     print("这条信息还不存在 程序将休眠30分钟，下次将判断编号：",num)
     time.sleep(1800)
    else:
        pass

    if check == checkYES:
        print("今日成功提交！ 八小时后程序再次启动")
        time.sleep(28800)
    else:
        pass
    num+=1
