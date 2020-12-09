#!/usr/bin/env python
# coding: utf-8

# In[59]:


import pandas as pd
from selenium import webdriver
from pyvirtualdisplay import display
from bs4 import BeautifulSoup
import lxml
import sys
import re
import time


# In[60]:


display = display.Display(visible=0, size=(1920, 1080)) 
display.start() 
path='./chromedriver' 


# In[61]:


chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--single-process")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--headless")  # Background(CLI) 동작 사용
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--remote-debugging-port=9222") 
driver = webdriver.Chrome(path, chrome_options=chrome_options)


# In[62]:


# !wget https://chromedriver.storage.googleapis.com/87.0.4280.20/chromedriver_linux64.zip
# !unzip chromedriver_linux64.zip
# !pip install lxml


# In[65]:


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
    if(i > 2):
        target = "https://www.ilbe.com"+str(link.get('href'))
#         print(target)
        driver.get(target)
        
        time.sleep(5)
        
        j = 2
        html = driver.page_source
        subPage = BeautifulSoup(target, "html.parser")
        prevarrow = driver.find_element_by_class_name("prev")
        print(target)
#         driver.execute_script("return $('loadComment(1)')[0]")
        driver.execute_script("arguments[0].click();", prevarrow)
        time.sleep(1)
        
        while(True):
            try:
                
#                 driver.execute_script("return $('loadComment("+str(j)+")')[0]")
                
                nextarrow = driver.find_element_by_link_text(str(i),)
#                 nextarrow = driver.find_element(By.onclick, 'loadComment('+j+')')
#                 driver.execute_script("arguments[0].click();", nextarrow)
                
                print("next page...")
#                 for arrow in subPage.drivers.findAll('a', atrrs={'onclick': re.compile("loadComment("+str(j)+")")}):
#                     print(arrow)
#                     print(j)
#                     j+=1
            except:
                print("break;;;;")
                break
       
    else:
        print("skipping AD...")
        print(i)
        i+=1
    


# In[ ]:




