# pip install selenium

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
 
driver = webdriver.Chrome() # 디렉토리 경로

url1 = "https://cafe.naver.com/joonggonara"
driver.get(url1)

driver.find_element_by_css_selector('#topLayerQueryInput').send_keys('오픈소스')
driver.find_element_by_css_selector('#topLayerQueryInput').send_keys(Keys.ENTER)


# <input title="카페글 검색어 입력" type="text" class="inp" name="query" style="ime-mode:active" id="topLayerQueryInput" onkeydown="if (event.keyCode == 13) {searchBoard();}">