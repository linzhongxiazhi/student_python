from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
"""初始化"""
# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
wd.implicitly_wait(10)#最大运行时间不超过10秒
wd.maximize_window() #最大化
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('http://172.31.132.227:8081/ism/main/index')
"""登录网页"""
username = wd.find_element_by_id('username') #获得账号和密码
password = wd.find_element_by_id('password')
username.send_keys('test')
password.send_keys("123456")
enter = wd.find_element_by_id("button_submit") #enter:登录
enter.click() #点击登录按钮

"""找到功能导航"""
专业知识 = wd.find_element_by_id("zTree_39_switch")
专业知识.click()
业务咨询 = wd.find_element_by_id("zTree_40_switch")
业务咨询.click()
"""定位到滚动条"""
滚动条 =wd.find_element_by_css_selector("[style='position: relative; top: 0px; float: right; width: 4px; height: 143px; background-color: rgb(166, 166, 166); border: 1px solid rgb(149, 149, 149); background-clip: padding-box; border-radius: 5px;']")
ActionChains(wd).drag_and_drop_by_offset(滚动条, 0, 120).perform() #滚动滚动条
功能导航 = wd.find_element_by_id("zTree_60_a")
功能导航.click()

"""新建"""
新建 = wd.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr/td[1]/div/h4/a')]").click()#文本单击
新建.click()