import requests as re
import json

def holiday(a):
    dictH={}
    try:
        year = str(a)
        key = '94ca56dfe74417cdfb8ace72a8e6d95c'
        r = re.get(f'http://v.juhe.cn/calendar/year?year={year}&key={key}')
        r_list = json.loads(r.text)
        holiday_list = r_list.get('result')['data']['holiday_list']
        for i in range(len(holiday_list)):
            if holiday_list[i]['name']=='元旦':
                h1=holiday_list[i]['startday']
                get_h_day(h1)
                dictH['元旦']=get_h_day(h1)
            if holiday_list[i]['name']=='春节':
                h2=holiday_list[i]['startday']
                get_h_day(h2)
                dictH['春节第一天']=get_h_day(h2)
                dictH['春节第二天']=get_h_day(h2)+1
                dictH['春节第三天']=get_h_day(h2)+2
            if holiday_list[i]['name']=='清明节':
                h3=holiday_list[i]['startday']
                get_h_day(h3)
                dictH['清明节']=get_h_day(h3)
            if holiday_list[i]['name']=='劳动节':
                h4=holiday_list[i]['startday']
                get_h_day(h4)
                dictH['劳动节']=get_h_day(h4)
            if holiday_list[i]['name']=='端午节':
                h5=holiday_list[i]['startday']
                get_h_day(h5)
                dictH['端午节']=get_h_day(h5)
            if holiday_list[i]['name']=='中秋节':
                h6=holiday_list[i]['startday']
                get_h_day(h6)
                dictH['中秋节']=get_h_day(h6)
            if holiday_list[i]['name']=='国庆节':
                h7=holiday_list[i]['startday']
                get_h_day(h7)
                dictH['国庆节第一天']=get_h_day(h7)
                dictH['国庆节第二天']=get_h_day(h7)+1
                dictH['国庆节第三天']=get_h_day(h7)+2
        return dictH
    except Exception:
        pass
def get_h_day(h):
    a=h.split('-')[0]
    b=h.split('-')[1]
    c=h.split('-')[2]
    h_day=get_total_days(a,b,c)
    return h_day

def leap_year(a):
    if (a % 4 == 0 and a % 100) != 0 or a % 400 == 0:
        return True
    else:
        return False
def year_days(a,b):
    if b in (1,3,5,7,8,10,12):
        return 31
    elif b in (4,6,9,11):
        return 30
    else:
        if leap_year(a)==True:
            return 29
        else:
            return 28
def get_total_days(a,b,c):
    a=int(a)
    b=int(b)
    c=int(c)
    total_days=0
    for m in range(1900,a):
        if leap_year(m)==True:
            total_days+=366
        else:
            total_days+=365
    for i in range(1,b):
        total_days+=year_days(a,i)
    total_days+=c
    return total_days



