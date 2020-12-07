from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from pandas import Series, DataFrame
import numpy as np
import pandas as pd
import re
import time

def ohou_crawling(url):
    driver_path = "driver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)

    # 페이지 이동
    url_page = url
    driver.get(url_page)
    time.sleep(1)

    #페이지 정보 획득
    title = str(driver.find_element_by_class_name('production-item__header__name').text)

    review = []
    dates = []
    # shoppings = []

    # 세부아이템 이동
    # i = 0
    time.sleep(5.5)
    soup = BeautifulSoup(driver.page_source, "lxml")
    for links in soup.find_all("a",{'class':'production-item__overlay'}):
        if 'href' in links.attrs:
            link = "https://ohou.se"+str(links.attrs['href'])
            print(link)
            driver.get(link)
            time.sleep(3.5)
            while(1):
                try:
                    html = driver.page_source
                    soup = BeautifulSoup(html, "lxml")
                    temp = re.sub('(<([^>]+)>)','$',str(soup.find_all('p', {'class':'production-review-item__description'})))
                    date = re.sub('(<([^>]+)>)','$',str(soup.find_all('span', {'class':'production-review-item__writer__info__date'})).replace("\n", ""))
                    for tem in temp.split('$'):
                        if(tem != ', ' and tem != ']' and tem != '['):
                            # print(tem.replace("\n", ""))
                            review.append(tem.replace("\n", ""))

                    for dat in date.split('$'):
                        if(dat != ', ' and dat != ']' and dat != '['):
                            tmp = []
                            # print(dat)
                            dat = dat.split(' ∙ ')

                            # print(dat[0])
                            # print(dat[1])
                            dates.append(dat[0])
                            # shoppings.append(dat[1])

                    driver.find_element_by_class_name('_2XI47._3I7ex').click()
                    time.sleep(1)

                except:
                    break
    print(len(review))
    print(len(dates))
    print(len(shoppings))
    output = pd.DataFrame({
        title: review,
        '구매일':dates
    })
    output.to_excel(excel_writer='./output/output.csv')

#오늘의 집 링크 입력 => query="Product_Name"
ohou_crawling("https://ohou.se/productions/feed?query=%EB%84%A4%EC%98%A4%ED%94%8C%EB%9E%A8")
