#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
from selenium import webdriver
from pyvirtualdisplay import display
from bs4 import BeautifulSoup
import lxml
import sys
import re
import time


# In[2]:


display = display.Display(visible=0, size=(1920, 1080)) 
display.start() 
path='./chromedriver' 


# In[3]:


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")  # Background(CLI) 동작 사용
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--remote-debugging-port=9222") 
driver = webdriver.Chrome(path, chrome_options=chrome_options)


# In[4]:


# !wget https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_linux64.zip
# !unzip chromedriver_linux64.zip
# !pip install lxml


# In[6]:


url_page = 'http://www.ilbe.com/ilbe'
driver.get(url_page)

Titles = []
Comments = []

# 일베 main 크롤링
# while page < 100:
# 타이틀 페이지 파싱
i = 1
html1 = driver.page_source
titlePage = BeautifulSoup(html1, "html.parser")

for link in titlePage.findAll('a', attrs={'href': re.compile("view")}):
    if(i > 2): #광고 제거
        #링크 이동
        target = "https://www.ilbe.com"+str(link.get('href'))
        driver.get(target)
        
        #대기
        time.sleep(5)
        
        html = driver.page_source
        subPage = BeautifulSoup(target, "html.parser")
        
        #맨 앞 버튼 = 페이지 특성 상 맨 뒤 코멘트 부터 보여줌
        prevarrow = driver.find_element_by_class_name("prev")
        driver.execute_script("arguments[0].click();", prevarrow)
        time.sleep(1)
        
        while(True):
            try:
                html = driver.page_source
                soup = BeautifulSoup(html, "html.parser")
                for com in soup.find_all('span', attrs={'class':re.compile('cmt')}):
                    print(com)
#                 comment = re.sub('(<([^>]+)>)', '$', str(soup.find_all('span':{'class':'cmt'})))
                
#                 for com in comment.split('$'):
#                     if com != ', ' and com != ']' and com != '[':
#                         print(com)
#                         Comments.append()
                
                #다음 버튼
#                 nextarrow = driver.find_element_by_link_text(str(i),)
                
                print("next page...")
                
            except:
                print("break;;;;")
                break
       
    else:
        print("skipping AD...")
        print(i)
        i+=1
    


# In[ ]:




