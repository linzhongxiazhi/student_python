from selenium import webdriver
wd = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
a = wd.find_elements_by_tag_name("div")
for i in a:
    print(i.text)