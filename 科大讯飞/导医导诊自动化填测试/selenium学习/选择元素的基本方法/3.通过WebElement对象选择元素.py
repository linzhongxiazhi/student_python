from selenium import webdriver
wd = webdriver.Chrome(r'd:\webdrivers\chromedriver.exe')
wd.get('http://cdn1.python3.vip/files/selenium/sample1.html')
element = wd.find_element_by_id('container')
spans = element.find_elements_by_tag_name("span")
for span in spans:
    print(span.text)

