from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")
    chrome = webdriver.Chrome(options=options, executable_path="C:/Users/Kevin/Desktop/chromedriver.exe")
    chrome.set_page_load_timeout(10)
    chrome.get("https://code-gym.github.io/spider_demo/")
    soup = BeautifulSoup(chrome.page_source, "html5lib")
    print(soup.find("h1").text)

    chrome.find_element(By.XPATH,'/html/body/div[2]/div/div[2]/div[3]/div/div/h3/a').click()
    print(chrome.find_element(By.XPATH,'//*[@id="post-header"]/div[2]/div/div/h1').text)
finally:
    chrome.quit()