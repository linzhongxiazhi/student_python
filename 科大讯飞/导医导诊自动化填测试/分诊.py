import time
from selenium import *
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
def log_in():
    global web
    web = webdriver.Chrome(r'd:\python\webdrivers\chromedriver.exe')
    web.implicitly_wait(10)  # 最大运行时间不超过10秒
    web.get('http://172.31.132.227:8081/ism/main/index')
    """登录网页"""
    username = web.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[2]/div/input')  # 获得账号和密码
    password = web.find_element_by_xpath('/html/body/div[2]/div[2]/form/div[3]/div/input')
    username.send_keys('test')
    password.send_keys("123456")
    enter = web.find_element_by_xpath("/html/body/div[2]/div[2]/form/div[4]/input[4]").click()  # enter:登录
def log_in_fenzheng():
    专业知识库 = web.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div/ul/li[3]/ul/li[2]/span").click()
    业务咨询 =web.find_element_by_xpath("/html/body/div[2]/div[2]/div[1]/div[2]/div[2]/div/ul/li[3]/ul/li[2]/ul/li[1]/span").click()
    enter_on =web.find_element_by_id("zTree_40_ul")
    enter_on_li =enter_on.find_elements_by_tag_name("li")
    for i in enter_on_li:
        web.execute_script("arguments[0].scrollIntoView();", i)
        if i.text == "分诊":
            i.click()

def new(text):
    iframe = web.find_element_by_class_name("lt-mainiframe")  # 定位到内嵌的iframe网页
    web.switch_to.frame(iframe)  # 切入到iframe
    # web.switch_to.default_content()  # 回到主页面，这一步一定要记得，有很多初学者会忘记写这一步导致无法定位到原页面元素
    新建 = web.find_element_by_class_name("barea-btn").click()  # 文本单击
    名称 = web.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr/td[1]/div/div[1]/table/tbody/tr[1]/td[2]/input").send_keys(text)
    保存 = web.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr/td[1]/div/div[1]/table/tbody/tr[2]/td[2]/a[1]/i[2]").click()
    添加自定义 = web.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr/td[2]/div[1]/div[1]/div/a[4]/i[2]").click()
    标准问 = web.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr/td[2]/div[2]/div/form/div[2]/input").send_keys("分诊")
    标准问同步加入句式 = web.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr/td[2]/div[2]/div/form/div[3]/input").click()
    高级设置 =  web.find_element_by_xpath("/html/body/div[2]/div/table/tbody/tr/td[2]/div[2]/div/form/div[2]/a").click()
    # 新建.click()



if __name__ == '__main__':
    text = "2"
    log_in()
    log_in_fenzheng()
    new(text)