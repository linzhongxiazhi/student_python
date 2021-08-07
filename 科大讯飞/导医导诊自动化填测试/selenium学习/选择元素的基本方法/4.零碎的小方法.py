from selenium import webdriver
wd = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
wd.get('http://cdn1.python3.vip/files/selenium/test3.html')
a = wd.find_element_by_id("input1")
a.clear()
a.send_keys("朱浩浩")

#获取输入框的文字
print(a.get_attribute("value"))

#获取元素文本内容
b = wd.find_element_by_css_selector("[style='color: brown']")
print(b.text)
#.text用不了可以用下面两种方法
print(b.get_attribute('innerText') )
print(b.get_attribute('textContent'))

#获取整个元素对应的HTML
print(b.get_attribute("outerHTML"))

"""获得元素属性"""
print(b.get_attribute("class"))