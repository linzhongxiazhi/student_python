from selenium import *
from selenium import webdriver
def log_in():
    global web
    web = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
    web.implicitly_wait(10)  # 最大运行时间不超过10秒
    # 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
    web.get('http://172.31.132.227:8081/ism/main/index')
    """登录网页"""
    username = web.find_element_by_id('username')  # 获得账号和密码
    password = web.find_element_by_id('password')
    username.send_keys('test')
    password.send_keys("123456")
    enter = web.find_element_by_css("button_submit")  # enter:登录
    enter.click()  # 点击登录按钮
    return web

if __name__ == '__main__':
    log_in()