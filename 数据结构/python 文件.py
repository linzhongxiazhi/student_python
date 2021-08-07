from selenium import webdriver
import time

web= webdriver.Chrome(r'D:\python\webdrivers\chromedriver.exe')
web.get('https://account.teambition.com/login')
en = web.find_element_by_xpath("/html/body/div/div[1]/div/div[3]/div[2]/div[1]/div[2]/div/input")
en.send_keys("18556376220")
time.sleep(2)
en1 = web.find_element_by_xpath("/html/body/div/div[1]/div/div[3]/div[2]/div[2]/button")
en1.click()
# if __name__=='__main__':
#     denglu()
#     denglu_2()
#     a1()
