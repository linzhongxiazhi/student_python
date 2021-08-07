from selenium import webdriver

# 创建 WebDriver 对象，指明使用chrome浏览器驱动
wd = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
# 调用WebDriver 对象的get方法 可以让浏览器打开指定网址
wd.get('https://www.baidu.com')
# 根据id选择元素，返回的就是该元素对应的WebElement对象
wd.find_element_by_id("kw").send_keys("朱浩浩")
wd.find_element_by_id("su").click()