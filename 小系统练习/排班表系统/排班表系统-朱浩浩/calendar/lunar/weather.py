import re
from bs4 import BeautifulSoup
import requests
import csv
import json
from  tkinter import *

class AppWeather:
    def __init__(self):
        self.windows = Tk()
        self.windows.title("天气")
        self.windows.geometry("300x600")
        self.creat_res()
        self.windows.mainloop()
    def creat_res(self):
        self.T1 = Text(self.windows)
        self.T1.place(x=0, y=0, relwidth=1, relheight=1)
        self.main()
    def get_page(self,url):
        try:
            kv = {'user-agent':'Mozilla/5.0'}
            r = requests.get(url,headers = kv)
            r.raise_for_status()
            r.encoding = r.apparent_encoding
            return r.text
        except:
            return '错误'

    def parse_page(self,html, return_list):
        soup = BeautifulSoup(html, 'html.parser')
        pattern = re.compile(r"var hour3data=(.*?)}", re.MULTILINE | re.DOTALL)
        script = soup.find("script", text=pattern)
        s = script.string
        s_7d = s.split('}')[0].split('"7d":')[1]
##        print (s_7d)
        dic_data = json.loads(s_7d, encoding='utf8')
        dic_data2 = dic_data
##        print(dic_data)
        for i in range(len(dic_data2)):
            for m in range(len(dic_data2[i])):
                self.T1.insert(END,f'{dic_data2[i][m]}\n')

    def main(self):
        url = 'http://www.weather.com.cn/weather/101280703.shtml'
        html = self.get_page(url)
        wea_list = []
        self.parse_page(html, wea_list)

