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

def cou_crawling():
    # driver init
    driver_path = "driver/chromedriver.exe"
    driver = webdriver.Chrome(executable_path=driver_path)
    reviews = {}
    review = []
    dates = []
    items = []

    for i in range(1, 14):
        url = "https://www.coupang.com/np/search?q=%EB%84%A4%EC%98%A4%ED%94%8C%EB%9E%A8&brand=&offerCondition=&filter=&availableDeliveryFilter=&filterType=&isPriceRange=false&priceRange=&minPrice=&maxPrice=&page="+str(i)+"&trcid=&traid=&filterSetByUser=true&channel=user&backgroundColor=&component=&rating=0&sorter=scoreDesc&listSize=72"

        try:
            url_page = url
            driver.get(url_page)
        except:
            print("부정확한 url입니다.")
            return -1

            # 이동 대기
        time.sleep(5.5)
        i = 0;
        # 세부아이템 url 수집
        soup = BeautifulSoup(driver.page_source, "lxml")


        for links in soup.find_all("a", {'class':'search-product-link'}):
            link = "https://coupang.com"+links.attrs['href']
            print(link)

            driver.get(link)

            html = driver.page_source
            soup = BeautifulSoup(html, "lxml")


            time.sleep(1)

            title = re.sub('(<([^>]+)>)', '', str(soup.find_all("h2", {'class':'prod-buy-header__title'})))

            if "네오플램" in title:

                print(title)

                reviewtab = driver.find_element_by_name('review')
                reviewtab.click()
                time.sleep(3)
                i = 2;
                while (True):
                    if(i==13):
                        i = 1;
                    html = driver.page_source
                    soup = BeautifulSoup(html, "html.parser")

                    temp = str(soup.find_all("div", {
                        'class': 'sdp-review__article__list__review__content js_reviewArticleContent'})).replace('<br/>', '').replace('<div class="sdp-review__article__list__review__content js_reviewArticleContent">', '$').replace('            </div>', '').replace('\n', '').replace('                                            ','').replace('                        ','')



                    for tem in temp.split('$'):
                        if tem != ', ' and tem != ']' and tem != '[':
                            review.append(tem.rstrip(', '))
                            items.append(title)
                            print(tem)

                    i = i+1

                    time.sleep(3)
                    # driver.find_element_by_class_name('sdp-review__article__page__num').click()

                    try:
                        driver.find_element_by_xpath(
                            '/html/body/div[1]/section/div[2]/div[10]/ul[2]/li[2]/div/div[5]/section[4]/div[3]/button[' + str(
                                i) + ']').click()
                    except:
                        break

            else:
                print("다음")

    reviews["품목"] = items
    reviews["리뷰"] = review

    output = pd.DataFrame.from_dict(reviews, orient='index').T
    output.to_excel(excel_writer='./output_coupang.xlsx')

cou_crawling()