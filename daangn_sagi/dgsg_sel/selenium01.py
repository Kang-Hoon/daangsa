'''

Date : Mar 3rd 2022
Reference : https://youtu.be/ZFmTwbRQ0uc

'''

# pip install selenium

from ast import While
from lib2to3.pgen2.token import OP
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import os
import time

chrome_options = Options()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome('/Users/yongmin/Documents/github/daangsa/daangn_sagi/dgsg_sel/chromedriver') # 디렉토리 경로

url1 = "https://www.google.co.kr"
driver.get(url1)

# driver.find_element_by_css_selector('.gLFyf.gsfi').send_keys('중고나라')
# driver.find_element_by_css_selector('').send_keys(Keys.ENTER)

time.sleep(1000)

'''
while(True) :
    pass
    '''