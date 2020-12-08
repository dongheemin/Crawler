from bs4 import BeautifulSoup
from urllib.request import urlopen
from selenium import webdriver
from pandas import Series, DataFrame
import numpy as np
import pandas as pd
import re
import time
import datetime

def doScrollDown(whileSecond, driver):
    start = datetime.datetime.now()
    end = start + datetime.timedelta(seconds=whileSecond)

    while True:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(1)
        if datetime.datetime.now() > end:
            break

def ohou_crawling(url, mode = 0):
    #driver init
    driver_path = "driver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)

    # mode selection
    if mode == 1:
        url += "&order=review"
    elif mode == 2:
        url += "&order=buy"

    # page 검사
    try:
        url_page = url
        driver.get(url_page)
    except:
        print("부정확한 url입니다.")
        return -1

    #이동 대기
    time.sleep(5.5)

    # 세부아이템 url 수집
    soup = BeautifulSoup(driver.page_source, "lxml")
    # doScrollDown(3, driver) #스크롤 다운기능
    for links in soup.find_all("a",{'class':'production-item__overlay'}):
        if 'href' in links.attrs:
            review = []
            dates = []
            link = "https://ohou.se"+str(links.attrs['href'])
            print(link)

            # 세부아이템 이동
            driver.get(link)
            time.sleep(3.5)

            #제목 수집
            html = driver.page_source
            soup = BeautifulSoup(html, "lxml")
            title = re.sub('(<([^>]+)>)','$',str(soup.find_all('span', {'class':'production-selling-header__title__name'})))

            #리뷰 수집
            while(1):
                try:
                    html = driver.page_source
                    soup = BeautifulSoup(html, "lxml")
                    temp = re.sub('(<([^>]+)>)','$',str(soup.find_all('p', {'class':'production-review-item__description'})))
                    date = re.sub('(<([^>]+)>)','$',str(soup.find_all('span', {'class':'production-review-item__writer__info__date'})).replace("\n", ""))
                    for tem in temp.split('$'):
                        if(tem != ', ' and tem != ']' and tem != '['):
                            review.append(tem.replace("\n", ""))

                    for dat in date.split('$'):
                        if(dat != ', ' and dat != ']' and dat != '['):
                            dat = dat.split(' ∙ ')
                            dates.append(dat[0])

                    driver.find_element_by_class_name('_2XI47._3I7ex').click() #다음버튼
                    time.sleep(1) #로딩 대기

                except:
                    break
    # print(len(review))
    # print(len(dates))
    # print(len(shoppings))
    output = pd.DataFrame({
        title: review,
        '구매일':dates
    })
    output.to_excel(excel_writer='./output_ohou.csv')

#오늘의 집 링크 입력 => query="Product_Name"
#mode = 0 (기본), mode = 1 (리뷰순), mode = 2 (판매순)
ohou_crawling("https://ohou.se/productions/feed?query=%EB%84%A4%EC%98%A4%ED%94%8C%EB%9E%A8", mode=1)
