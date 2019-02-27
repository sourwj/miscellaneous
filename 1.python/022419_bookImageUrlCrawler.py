import time
import requests
import lxml.html
import re
import time
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By #https://www.seleniumhq.org/docs/03_webdriver.jsp#locating-ui-elements-webelements

#검색 page가 로딩 되는 시간을 대기하기 위한 모듈
from selenium.webdriver.support.ui import WebDriverWait

# 예외 처리를 위한 모듈
from selenium.webdriver.support import expected_conditions as EC

import csv

results = []
titleList = []
with open('titles5_700-799.csv', "r", encoding="utf-8") as f:
    for i in f.readlines():
        titleList.append(i)
print(titleList)
print('----------------------')
for j in range(len(titleList)):
    driver = webdriver.Chrome("C:/driver/chromedriver.exe")
    keyword = titleList[j]
    url = "https://www.aladin.co.kr/home/welcome.aspx"
    driver.get(url)
    time.sleep(2)
    driver.implicitly_wait(5)
    elem = driver.find_element_by_id("SearchWord")
    elem.clear()
    elem.send_keys(keyword)
    btn_search = driver.find_element_by_xpath('//*[@id="global_search"]/input')
    btn_search.click()
    soup = BeautifulSoup(driver.page_source, "html.parser" )
    items = soup.select('.ss_book_box')
    img_src = items[0].find('img')['src']
    print(img_src)
    results.append(img_src)
time.sleep(1)
driver.close()

with open('L_700-799', 'w', encoding = 'utf-8') as f:
    csv_writer = csv.writer(f)
    for result in results:
        csv_writer.writerows([result])