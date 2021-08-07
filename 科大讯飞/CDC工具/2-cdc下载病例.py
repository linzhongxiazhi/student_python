from selenium import webdriver
import time
import datetime
import os
import openpyxl as vb
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains

def deconnexion(Chrome):
    """登陆"""
    """初始化"""
    global web, actions
    web = webdriver.Chrome(Chrome) #公司电脑
    # web = webdriver.Chrome(r'D:\python\webdrivers\chromedriver.exe') #自己的电脑
    web.maximize_window()
    web.implicitly_wait(10)  # 最大运行时间不超过10秒
    web.get('http://www.wjw-cdc.com:8003/user-center-portal/login?redirect=%2Fmain')
    actions = ActionChains(web)

    """登录网页"""
    username = web.find_element_by_xpath('/html/body/div/div/div[1]/div/div[2]/form/div[1]/div/div[1]/input')  # 获得账号和密码
    password = web.find_element_by_xpath('/html/body/div/div/div[1]/div/div[2]/form/div[2]/div/div[2]/input')
    username.send_keys('15375429564')
    password.send_keys("cdc1234cdc")
    enter = web.find_element_by_xpath("/html/body/div/div/div[1]/div/div[2]/form/div[3]/div/button")
    enter.click()
    return 0
def menu_lien():
    """跳转页面"""
    enter_into = web.find_element_by_xpath(
        "/html/body/div[1]/div/div[2]/section/div/div[1]/ul/li[1]/ul/li[2]/span/div[2]/section/article")
    enter_into.click()
    return 0
def confirm_area(city, area):
    """确定区域"""
    """点击区域"""
    enter_area = web.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/div[1]/span/div/div[1]/input").click()
    """点击安徽省"""
    enter_on_on = web.find_element_by_class_name("el-cascader__dropdown")
    enter_on = enter_on_on.find_element_by_class_name("el-cascader-panel")
    try:
        enter_AnHui_on_on = enter_on.find_elements_by_class_name("el-scrollbar")
        enter_AnHui_on =enter_AnHui_on_on[0].find_element_by_class_name("el-scrollbar__view")
    except:
        time.sleep(1)
        enter_AnHui_on_on = enter_on.find_elements_by_class_name("el-scrollbar")
        enter_AnHui_on = enter_AnHui_on_on[0].find_element_by_class_name("el-scrollbar__view")
    enter_AnHui = enter_AnHui_on.find_element_by_tag_name("li")
    enter_AnHui_down =enter_AnHui.find_element_by_class_name("el-radio__input")
    web.execute_script("arguments[0].click();", enter_AnHui_down)
    """选择城市"""
    enter_on_on = web.find_element_by_class_name("el-cascader__dropdown")
    enter_on = enter_on_on.find_element_by_class_name("el-cascader-panel")
    try:
        enter_city_on_on =enter_on.find_elements_by_class_name("el-scrollbar")
        enter_city_on = enter_city_on_on[1].find_element_by_class_name("el-cascader-menu__wrap")
    except:
        time.sleep(1)
        enter_city_on_on = enter_on.find_elements_by_class_name("el-scrollbar")
        enter_city_on = enter_city_on_on[1].find_element_by_class_name("el-cascader-menu__wrap")
    enter_city = enter_city_on.find_elements_by_tag_name("li")
    for i in range(len(enter_city)):
        enter_on_on = web.find_element_by_class_name("el-cascader__dropdown")
        enter_on = enter_on_on.find_element_by_class_name("el-cascader-panel")
        enter_city_on_on = enter_on.find_elements_by_class_name("el-scrollbar")
        enter_city_on = enter_city_on_on[1].find_element_by_class_name("el-cascader-menu__wrap")
        enter_city = enter_city_on.find_elements_by_tag_name("li")
        if enter_city[i].text ==city:
            enter_city_down = enter_city[i].find_element_by_class_name("el-radio__input")
            web.execute_script("arguments[0].click();", enter_city_down)
            break
    """选则区县"""
    enter_on_on = web.find_element_by_class_name("el-cascader__dropdown")
    enter_on = enter_on_on.find_element_by_class_name("el-cascader-panel")
    try:
        enter_area_on_on =enter_on.find_elements_by_class_name("el-scrollbar")
        enter_area_on = enter_area_on_on[2].find_element_by_class_name("el-cascader-menu__wrap")
    except:
        time.sleep(1)
        enter_area_on_on = enter_on.find_elements_by_class_name("el-scrollbar")
        enter_area_on = enter_area_on_on[2].find_element_by_class_name("el-cascader-menu__wrap")
    enter_area = enter_area_on.find_elements_by_tag_name("li")
    for i in range(len(enter_area)):
        enter_on_on = web.find_element_by_class_name("el-cascader__dropdown")
        enter_on = enter_on_on.find_element_by_class_name("el-cascader-panel")
        enter_area_on_on = enter_on.find_elements_by_class_name("el-scrollbar")
        enter_area_on = enter_area_on_on[2].find_element_by_class_name("el-cascader-menu__wrap")
        enter_area = enter_area_on.find_elements_by_tag_name("li")
        if enter_area[i].text ==area:
            enter_area_down = enter_area[i].find_element_by_class_name("el-radio__input")
            web.execute_script("arguments[0].click();", enter_area_down)
            break

    return 0
def confirm_time_on(excel_time):
    if type(excel_time) == str:
        return str(excel_time)
    elif type(excel_time) == datetime.datetime:
        excel_time_2 = excel_time.strftime('%Y-%m-%d')
        return str(excel_time_2)
def confirm_tiem(time):
    """确定时间"""
    time =confirm_time_on(time)
    enter_time = web.find_elements_by_class_name("el-range-input")
    for i in enter_time:
        i.send_keys(time)
    return 0
def confirm_cause(cause):
    """选则症状"""
    enter_symptom = web.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/div[3]/span/div/div[2]/input").click()
    enter_on = web.find_element_by_class_name("is-multiple")
    enter_on_1 =enter_on.find_element_by_class_name("el-scrollbar")
    enter_on_symptom = enter_on_1.find_elements_by_tag_name("li")
    for i in range(len(enter_on_symptom)):
        enter_on = web.find_element_by_class_name("is-multiple")
        enter_on_symptom = enter_on.find_elements_by_tag_name("li")
        if enter_on_symptom[i].text == cause:
            enter_on_symptom[i].click()
            break
    return 0
def search():
    """点击搜索"""
    enter_search = web.find_element_by_xpath("/html/body/div[1]/section/main/div/div[3]/button[1]").click()
    return 0
def reset():
    """点击重置"""
    enter_reset = web.find_element_by_xpath("/html/body/div/section/main/div/div[3]/button[2]").click()
    return 0
def pending():
    """待处理"""
    enter_pending = web.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div[4]/div/div[1]/div/div/div/div[1]").click()
    return 0
def accomplish():
    """已完成"""
    enter__accomplish = web.find_element_by_xpath(
        "/html/body/div[1]/section/main/div/div[4]/div/div[1]/div/div/div/div[3]").click()
    return 0
def download_cas():
    """下载病例"""
    enter_download_cas = web.find_element_by_xpath(
        "/html/body/div[1]/section/main/section/main/div[2]/ul/li[2]").click()
    enter_download_cas_1 = web.find_element_by_xpath(
        "/html/body/div[1]/section/main/section/main/div[2]/div/div[2]/div/div[1]/div/button[3]").click()
    return 0
def resetting_excel(cause, clinique, path="D:\林钟\下载"):
    """重命名病例"""
    try:
        files = os.listdir(path)
        src = path + "\\" + "外呼结果导出表格.xlsx"
        if cause =="发热伴畏寒|寒战":
            cause ="发热伴畏寒寒战'"
        if cause == "畏寒|寒战":
            cause = "畏寒寒战'"
        dst = path + "\\" + clinique + "--" + cause + ".xlsx"
        os.rename(src, dst)
    except (FileExistsError):
        files = os.listdir(path)
        src = path + "\\" + "外呼结果导出表格.xlsx"
        if cause =="发热伴畏寒|寒战":
            cause ="发热伴畏寒寒战'"
        if cause == "畏寒|寒战":
            cause = "畏寒寒战'"
        dst = path + "\\" + clinique + "--" + cause + ".xlsx"
        os.remove(dst)
        os.rename(src, dst)

    return 0
def pagination(): #获取当前界面一共有多少条数据
    pagination__total = web.find_element_by_xpath("/html/body/div[1]/section/main/div/div[5]/span[1]")
    a = int(pagination__total.text[2:-2])
    return a
def search_data(cause, city, area, clinique, excel_time):
    """查找数据"""
    ls_2 =[] #存储最终点击的元素，如果为空则说明没找到。
    trlist_table_on = web.find_element_by_class_name("is-scrolling-none")
    trlist_table = trlist_table_on.find_element_by_class_name("el-table__body")
    trlist_tr = trlist_table.find_elements_by_tag_name("tr")
    for row in range(len(trlist_tr)):
        trlist_table = web.find_element_by_class_name("el-table__body")
        trlist_tr = trlist_table.find_elements_by_tag_name("tr")
        trlist_td = trlist_tr[row].find_elements_by_tag_name("td")
        i = 0
        j = 0
        ls = []
        for col in range(len(trlist_td)):
            i += 1
            if i == 2:
                ls.append(trlist_td[col].text)
            elif i == 3:
                ls.append(trlist_td[col].text)
            elif i == 7:
                ls.append(trlist_td[col])
            elif i == 9:
                j = 1
                ls.append((trlist_td[col]))
            trlist_td = trlist_tr[row].find_elements_by_tag_name("td")
        if ls[0] == cause:
            if ls[1] == ("安徽省/" + city + "/" + area + "/" + clinique):
                if j == 0:
                    # ls[2].click()
                    ls_2.append(ls[2])
                elif j == 1:
                    # ls[3].click()
                    ls_2.append(ls[3])
    return ls_2
def search_data_down(cause,clinique,path):
    """找到病例后的对病例进行一系列的处理"""
    """下载病例"""
    download_cas()
    """返回上一界面"""
    web.back()
    """点击重置"""
    reset()
    """点击待完成"""
    pending()
    """给病例重命名"""
    time.sleep(2)
    try:
        resetting_excel(cause, clinique,path)
    except FileNotFoundError:
        time.sleep(2)
        resetting_excel(cause, clinique,path)
    print(clinique + "--" + cause + "已下载完成！")
def tourne_page():
    enter_tourne_page =web.find_element_by_xpath("/html/body/div[1]/section/main/div/div[5]/button[2]/i").click()
    return ""
def search_data_on(cause, city, area, clinique, excel_time,path):
    """核心处理流程"""
    time.sleep(2)
    number = pagination()
    """判断待处理下标是否为0"""
    if number == 0 :
        """点击已完成"""
        accomplish()
        time.sleep(2)
        number_accmplish_1 = pagination()
        """判断已完成的下标是否为0"""
        if number_accmplish_1 == 0:
            """如果为0下载失败"""
            download_revers.append(clinique + "--" + cause + " 下载失败！")
        else:
            """不为0判断当前界面是否只有20条数据"""
            if 0 < number_accmplish_1 <= 20:
                """只有20条数据查找数据"""
                accomplish_search_data = search_data(cause, city, area, clinique, excel_time)
                if len(accomplish_search_data) == 0:
                    """如果没找到结束"""
                    download_revers.append(clinique + "--" + cause + " 下载失败！")
                    reset()
                else:
                    """如果找到则点击"""
                    accomplish_search_data[0].click()
                    search_data_down(cause,clinique,path)
            elif 20 < number_accmplish_1 <= 40:
                """多于20条数据"""
                accomplish_search_data = search_data(cause, city, area, clinique, excel_time)
                """判断第一页有没有查到"""
                if len(accomplish_search_data) == 0:
                    """如果没找到翻页"""
                    tourne_page()
                    accomplish_search_data = search_data(cause, city, area, clinique, excel_time)
                    """判断翻页后有没有找到"""
                    if len(accomplish_search_data) == 0:
                        """如果没找到存入列表"""
                        download_revers.append(clinique + "--" + cause + " 下载失败！")
                        reset()
                    else:
                        """找到后点击"""
                        accomplish_search_data[0].click()
                        search_data_down(cause,clinique,path)
            else:
                download_revers.append(clinique + "--" + cause + " 下载失败！")
                reset()
    else:
        """判断待处理里是否小于20条数据"""
        if  0 < number <= 20:
            """如果小于进行查找"""
            pending__search_data = search_data(cause, city, area, clinique, excel_time)
            """判断有没有找到"""
            if len(pending__search_data) == 0:
                """没找到"""
                """点击已完成"""
                accomplish()
                time.sleep(2)
                number_accmplish_1 = pagination()
                """判断已完成的下标是否为0"""
                if number_accmplish_1 == 0:
                    """如果为0下载失败"""
                    download_revers.append(clinique + "--" + cause + " 下载失败！")
                else:
                    """不为0判断当前界面是否只有20条数据"""
                    if 0 < number_accmplish_1 <= 20:
                        """只有20条数据查找数据"""
                        accomplish_search_data = search_data(cause, city, area, clinique, excel_time)
                        if len(accomplish_search_data) == 0:
                            """如果没找到结束"""
                            download_revers.append(clinique + "--" + cause + " 下载失败！")
                            reset()
                        else:
                            """如果找到则点击"""
                            accomplish_search_data[0].click()
                            search_data_down(cause, clinique, path)
                    elif 20 < number_accmplish_1 <= 40:
                        """多于20条数据"""
                        accomplish_search_data = search_data(cause, city, area, clinique, excel_time)
                        """判断第一页有没有查到"""
                        if len(accomplish_search_data) == 0:
                            """如果没找到翻页"""
                            tourne_page()
                            accomplish_search_data = search_data(cause, city, area, clinique, excel_time)
                            """判断翻页后有没有找到"""
                            if len(accomplish_search_data) == 0:
                                """如果没找到存入列表"""
                                download_revers.append(clinique + "--" + cause + " 下载失败！")
                                reset()
                            else:
                                """找到后点击"""
                                accomplish_search_data[0].click()
                                search_data_down(cause, clinique, path)
                    else:
                        download_revers.append(clinique + "--" + cause + " 下载失败！")
                        reset()
            else:
                """找到了"""
                pending__search_data[0].click()
                search_data_down(cause,clinique,path)

        # elif 20< number <= 40:
        #     pending__search_data = search_data(cause, city, area, clinique, excel_time)
        #     """判断有没有找到"""
        #     if len(pending__search_data) == 0:


if __name__ == "__main__":

    download_revers = []
    """初始化"""
    url = input("请输入文件的绝对路径：") #文件路径
    path = "D:\林钟\下载" # 下载路径
    Chrome = r'D:\PYthon\webdrivers\chromedriver.exe' #驱动路径
    time1 = time.time()
    """登录页面"""
    deconnexion(Chrome)
    print("已登陆")
    menu_lien()
    print("已跳转")

    """读取表格"""
    excel = vb.load_workbook(url)
    sheet = excel["1-每日监控告警明细"]
    subscript = 1
    for i in sheet.iter_rows(min_row=2, max_row=101, max_col=1):
        for cell in i:
            if cell.value in ["3", 3, "高"]:

                """初始化数值"""
                cause = sheet["I" + str(cell.row)].value
                city = sheet["E" + str(cell.row)].value
                area = sheet["F" + str(cell.row)].value
                clinique = sheet["G" + str(cell.row)].value
                excel_time = sheet["D" + str(cell.row)].value

                """搜索"""
                try:
                    confirm_area(city, area)
                    confirm_tiem(excel_time)
                    confirm_cause(cause)
                    search()
                except:
                    try:
                        web.refresh()  # 刷新方法 refresh
                        print('刷新成功')
                        confirm_area(city, area)
                        confirm_tiem(excel_time)
                        confirm_cause(cause)
                        search()
                    except Exception as e:
                        print("刷新失败！", format(e))


                """查找数据"""
                search_data_on(cause, city, area, clinique, excel_time, path)


    """打印最终结果"""
    print("")
    print("<-----------下面是下载失败的----------->")
    for i in download_revers:
        print(i)
    print("已全部下载完毕")
    time2 = time.time()
    print("用时：{:.2f} 秒".format(time2-time1))