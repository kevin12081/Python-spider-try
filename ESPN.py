from bs4 import BeautifulSoup
from selenium import webdriver
import time
import random

url = 'https://insider.espn.com/nba/hollinger/statistics/_/page/'

try:
    options = webdriver.ChromeOptions()
    options.add_argument('--headless')
    chrome = webdriver.Chrome(options=options, 
                             executable_path="C:/Users/Kevin/Desktop/chromedriver.exe")
    chrome.set_page_load_timeout(10)
    for i in range(1, 9):
        _url = url + str(i)
        print(_url)
        chrome.get(_url)
        soup = BeautifulSoup(chrome.page_source, "html5lib")
        trs = soup.find("tbody").find_all('tr')
        for tr in trs:
            tds = [td for td in tr.children]
            rk = tds[0].text.strip()
            if rk =="RK" or len(tds)<2:
                continue
            name = tds[1].text
            per = tds[11].text
            print("%s :%s" % (name, per))
        wait = random.randint(2,6)
        print("wait time : %d" % wait )
        time.sleep(wait)
finally:
    chrome.quit()
