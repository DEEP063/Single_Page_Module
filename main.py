# This is a sample Python script.
import os
import time

import requests


#HERO
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiS-raNmuyDAxU-wzgGHSj3C6EQPAgJ")
# driver.find_element(By.ID,"APjFqb").send_keys("fewefwf")
# webdriver.ActionChains(driver).send_keys(Keys.ENTER).perform()
# time.sleep(5)


# # Application commands
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://www.google.com/webhp?hl=en&sa=X&ved=0ahUKEwiS-raNmuyDAxU-wzgGHSj3C6EQPAgJ")
# act_title = driver.title
# act_currenturl = driver.current_url
# act_source = driver.page_source
#
# print(act_title)
# print(act_currenturl)
# print(act_source)

# # conditional commands
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
#
# dis = driver.find_element(By.ID,"FirstName").is_displayed()
# ena = driver.find_element(By.ID,"FirstName").is_enabled()
# sel = driver.find_element(By.ID,"gender-male").is_selected()
# driver.find_element(By.ID,"gender-female").click()
# sel2 = driver.find_element(By.ID,"gender-female").is_selected()
#
# print(dis)
# print(ena)
# print(sel)
# print(sel2)
# time.sleep(7)

# # Navigational commands
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.common.keys import Keys
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# driver.find_element(By.LINK_TEXT,"Log in").click()
# driver.back()
# driver.forward()
# time.sleep(3)
# driver.refresh()
# time.sleep(4)


# # Wait
# # Implicit wait : it waits for every statements in code but we define it first
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.implicitly_wait(10) #Now onwards it wait for 10sec for every statement
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# driver.find_element(By.LINK_TEXT,"Log in").click()


# # Wait
# # Explicit wait : It waits until specfic conditions
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
#
# driver = webdriver.Chrome()
# wait = WebDriverWait(driver,10,poll_frequency=2,ignored_exceptions=[Exception])
#
#
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# wait.until(EC.presence_of_element_located((By.LINK_TEXT,"Log in"))).click()
# time.sleep(5)


# # Links:
# # 1> internal link 2>Externak kink and 3> Broken link
# from selenium import webdriver
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Chrome()
# driver.maximize_window()
# url = "http://www.deadlinkcity.com/"
# driver.get(url)
# links = driver.find_elements(By.TAG_NAME,"a")
#
# count = 0
# for link in links:
#     try:
#         href = link.get_attribute("href")
#         response = requests.head(href)
#     except:
#         None
#
#     if (response.status_code >= 400):
#         print(f"{href} is a broken link")
#         count = count+1
#     else:
#         print(f"{href} is a valid link")
#
# print(count)

# # Select Dropdown
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
# driver = webdriver.Chrome()
#
#
# driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
# select = Select(driver.find_element(By.ID,"country"))
#
# select.select_by_index(5)
# time.sleep(5)
#
# select.select_by_visible_text("France")
# time.sleep(5)
#
# select.select_by_value("uk")
# time.sleep(5)
#
# all_options = select.options
# for option in all_options:
#     print(option.text)

# # Alerts
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# driver.get("https://testpages.eviltester.com/styled/alerts/alert-test.html")
# driver.find_element(By.ID, 'promptexample').click()
# time.sleep(5)
# alert_window = driver.switch_to.alert
#
# print(alert_window.text)
#
# alert_window.send_keys("welcome")
# time.sleep(5)
# alert_window.accept()
# time.sleep(5)
#
# driver.find_element(By.ID, 'promptexample').click()
# time.sleep(5)
# alert_window = driver.switch_to.alert
# alert_window.send_keys("welcome2")
# alert_window.dismiss()
# time.sleep(6)

# # Frames : by nsmr,id,webelement,index
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# driver.get("https://javadoc.io/static/org.seleniumhq.selenium/selenium-api/2.50.1/index.html?org/openqa/selenium/SearchContext.html")
#
# driver.switch_to.frame("packageListFrame")
# driver.find_element(By.XPATH,"//a[contains(text(),'html5')]").click()
# driver.switch_to.default_content()
# time.sleep(4)
#
# driver.switch_to.frame("packageFrame")
# driver.find_element(By.XPATH,"//span[contains(text(),'WebStorage')]").click()
# driver.switch_to.default_content()
# time.sleep(4)
#
# driver.switch_to.frame("classFrame")
# driver.find_element(By.XPATH,"//a[contains(text(),'Index')]").click()
# driver.switch_to.default_content()
# time.sleep(4)


# # # Browsers : current_window , window_handles
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# time.sleep(4)
# driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
# time.sleep(3)
# driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
# time.sleep(3)
# driver.find_element(By.LINK_TEXT,"OrangeHRM, Inc").click()
# time.sleep(3)
# all_browsers = driver.window_handles
# for x in all_browsers:
#     print(x)
# print("################")
# driver.switch_to.window(all_browsers[1])
# driver.close()
# all_browsers = driver.window_handles
# for x in all_browsers:
#     print(x)
# print("################")
# driver.switch_to.window(all_browsers[0])
# print(driver.current_window_handle)
# time.sleep(6)


# # Pop Up
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
# options = webdriver.ChromeOptions()
# options.add_argument("--disable-notifications")
# driver = webdriver.Chrome(options=options)
#
# driver.maximize_window()
# driver.get("https://qa.agilityhealthradar.com/account/login")
# time.sleep(3)


# # # Basic Table
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
#
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# driver.get("https://testautomationpractice.blogspot.com/")
# total_rows = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr")
# total_cols = driver.find_elements(By.XPATH,"//table[@name='BookTable']/tbody/tr[2]/td")
#
# for r in range(2,len(total_rows)+1):
#     for c in range(1,len(total_cols)+1):
#         print(driver.find_element(By.XPATH,"//table[@name='BookTable']/tbody/tr["+str(r)+"]/td["+str(c)+"]").text,end="     ")
#     print()
#
# time.sleep(3)


# # # # Action class
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains
#
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# # driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
# # driver.find_element(By.NAME,"username").send_keys("Admin")
# # driver.find_element(By.NAME,"password").send_keys("admin123")
# # driver.find_element(By.XPATH,"//button[@type='submit']")
#
# driver.get("https://www.orangehrm.com/")
# time.sleep(4)
# act = ActionChains(driver)
#
# act.move_to_element(driver.find_element(By.LINK_TEXT,"Solutions")).perform()
# time.sleep(4)
# act.move_to_element(driver.find_element(By.XPATH,"//*[@id='navbarSupportedContent']/ul/li[1]/div/div/div/div/ul/li[1]")).click().perform()
# time.sleep(5)
# # act.move_to_element(driver.find_element(By.XPATH,"//h6[1]/a")).click().perform()
#
# # act.move_to_element(driver.find_element(By.XPATH,"//img[@class='wikipedia-icon']")).perform()
#
# driver.get("https://testautomationpractice.blogspot.com/")
#
# act.move_to_element(driver.find_element(By.ID,'name')).context_click().perform()
# time.sleep(5)
# act.move_to_element(driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")).double_click().perform()
# time.sleep(3)
#
# act.drag_and_drop(driver.find_element(By.ID,"draggable"),driver.find_element(By.ID,"droppable")).perform()
# time.sleep(3)
#
# box = driver.find_element(By.XPATH,"//div[@id='slider']/span")
#
# act.drag_and_drop_by_offset(box,-20,0)
# time.sleep(13)
#



# # # Scroll
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains
# #
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# driver.get("https://history.state.gov/countries/all")
#
# # driver.execute_script("window.scrollBy(0,3000)","")
# # time.sleep(3)
# # value = driver.execute_script("return window.pageYOffset;")
# # print(value)
#
# # flag = driver.find_element(By.XPATH,"//*[@id='content-inner']/div/div[1]/div[3]/ul/li[18]/a")
# # driver.execute_script("arguments[0].scrollIntoView();",flag)
# # time.sleep(3)
# # value = driver.execute_script("return window.pageYOffset;")
# # print(value)
#
# # Endpoint
# driver.execute_script("window.scrollBy(0,document.body.scrollHeight)","")
# time.sleep(3)
# value = driver.execute_script("return window.pageYOffset;")
# print(value)
#
# # Startpoint
# driver.execute_script("window.scrollBy(0,-document.body.scrollHeight)","")
# time.sleep(3)
# value = driver.execute_script("return window.pageYOffset;")
# print(value)
#

# # # Keyboard
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains, Keys
#
# #
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# driver.get("http://textcompare.com/")
# one = driver.find_element(By.XPATH,"//textarea[@name='frm_compare_1']")
# two = driver.find_element(By.XPATH,"//textarea[@name='frm_compare_2']")
#
# one.send_keys("Welcomw")
#
# act =ActionChains(driver)
# act.key_down(Keys.CONTROL).send_keys("a").key_up(Keys.CONTROL).perform()
# act.key_down(Keys.CONTROL).send_keys("c").key_up(Keys.CONTROL).perform()
# act.send_keys(Keys.TAB).perform()
# act.key_down(Keys.CONTROL).send_keys("v").key_up(Keys.CONTROL).perform()
# time.sleep(3)

# # # # Save Screenshot
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains, Keys
#
# #
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# driver.get("http://textcompare.com/")
#
# driver.save_screenshot(f"{os.getcwd()}\\xyzq.png")
# # driver.save_screenshot("C:\\Users\\SAI-PC\\PycharmProjects\\SimpleOneModule\\xyz.png")

# # # taab and window
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains, Keys
#
# #
# driver = webdriver.Chrome()
#
# driver.maximize_window()
# #for tab
# driver.get("http://textcompare.com/")
# driver.switch_to.new_window('tab')
# driver.get("http://textcompare.com/")
# time.sleep(4)
# #for window
# driver.get("http://textcompare.com/")
# driver.switch_to.new_window('window')
# driver.get("http://textcompare.com/")
# time.sleep(4)
# Open link in new tab
# driver.get("http://textcompare.com/")
# reglink = Keys.CONTROL+Keys.ENTER
# driver.find_element(By.XPATH,"//*[@id='navigation']/li[4]/a").send_keys(reglink)
# time.sleep(4)

# # # # Cookies
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains, Keys
#
# #
# driver = webdriver.Chrome()
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# # driver.get("https://qa.agilityhealthradar.com/account/login")
# cookies = driver.get_cookies()
# print(len(cookies))
# # for c in cookies:
# #     print(c)
# for c in cookies:
#     print(c.get('name'),":",c.get('value'),":",c.get('expiry'))
#     # print(f"{c.get('name')}:{c.get('value')}:{c.get('expiry')}")
# time.sleep(4)
# driver.delete_all_cookies()
# print(len(cookies))
# # for c in cookies:
# #     print(c)
# for c in cookies:
#     print(c.get('name'),":",c.get('value'),":",c.get('expiry'))
# driver.add_cookie({"name": "xyz", "value": "123"})
# print(len(cookies))
# # for c in cookies:
# #     print(c)
#
# for c in cookies:
#     print(c.get('name'),":",c.get('value'),":",c.get('expiry'))
#     # print(f"{c.get('name')}:{c.get('value')}:{c.get('expiry')}")


# # # Headless
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support.select import Select
# from selenium.webdriver import ActionChains, Keys
#
# ops = webdriver.ChromeOptions()
# ops.add_argument('--headless')
# driver = webdriver.Chrome(options=ops)
# driver.maximize_window()
# driver.get("https://demo.nopcommerce.com/register?returnUrl=%2F")
# time.sleep(3)

# #Read Excel
# import openpyxl
#
# file = f"{os.getcwd()}\\Book1.xlsx"
# # file = "C:\\Users\\SAI-PC\\PycharmProjects\\SimpleOneModule\\Book1.xlsx"
# workbook = openpyxl.load_workbook(file)
# sheet = workbook.active
# # sheet = workbook["Sheet1"]
#
# row = sheet.max_row
# col = sheet.max_column
#
# print(row)
# print(col)
# print(sheet.cell(1,1))
#
# for r in range(1,row+1):
#     for c in range(1,col+1):
#         print(sheet.cell(r,c).value,end="   ")
#     print()
#

# #Write excel
# import openpyxl
#
# file = f"{os.getcwd()}\\Book2.xlsx"
# # file = "C:\\Users\\SAI-PC\\PycharmProjects\\SimpleOneModule\\Book1.xlsx"
# workbook = openpyxl.load_workbook(file)
# sheet = workbook.active
# # sheet = workbook["Sheet1"]
#
# for r in range(1,4):
#     for c in range(1,5):
#         sheet.cell(r,c).value = "tenet"
#
# workbook.save(file)


#Data driven in Excel

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.select import Select
from selenium.webdriver import ActionChains, Keys

#
driver = webdriver.Chrome()
driver.implicitly_wait(10)
driver.maximize_window()
driver.get("https://www.moneycontrol.com/fixed-income/calculator/state-bank-of-india/fixed-deposit-calculator-SBI-BSB001.html")

driver.back()
time.sleep(2)
driver.forward()
time.sleep(2)
driver.refresh()
import XLS as x
file = f"{os.getcwd()}\\Book3.xlsx"
rows = x.getRowCount(file,"Sheet1")

for r in range(2,rows+1):
    pric = x.readData(file,"Sheet1",r,1)
    roi = x.readData(file,"Sheet1",r,2)
    per1 = x.readData(file,"Sheet1",r,3)
    per2 = x.readData(file,"Sheet1",r,4)
    fre = x.readData(file,"Sheet1",r,5)
    ex = x.readData(file,"Sheet1",r,6)

    driver.find_element(By.XPATH,'//*[@id="principal"]').send_keys(pric)
    driver.find_element(By.XPATH,'//*[@id="interest"]').send_keys(roi)
    driver.find_element(By.XPATH,'//*[@id="tenure"]').send_keys(per1)

    predrop = Select(driver.find_element(By.XPATH,'//*[@id="tenurePeriod"]'))
    predrop.select_by_visible_text(per2)

    fredrop = Select(driver.find_element(By.XPATH,'//*[@id="frequency"]'))
    fredrop.select_by_visible_text(fre)

    driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[1]/img').click()

    acc = driver.find_element(By.XPATH,'//*[@id="resp_matval"]/strong').text

    if float(ex) == float(acc):
        x.writeData(file,"Sheet1",r,8,"Passed")
        x.fillGreenCoolor(file,"Sheet1",r,8)
    else:
        x.writeData(file,"Sheet1",r,8,"Failed")
        x.fillRedCoolor(file,"Sheet1",r,8)

    driver.find_element(By.XPATH,'//*[@id="fdMatVal"]/div[2]/a[2]/img').click()
    time.sleep(2)












































