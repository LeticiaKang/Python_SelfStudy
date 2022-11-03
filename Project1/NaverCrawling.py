from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys #키보드
from selenium.webdriver.common.by import By
from selenium import webdriver
import pandas as pd #엑셀화 판다스
from bs4 import BeautifulSoup as bs
import pyperclip
import time

driver = webdriver.Chrome(ChromeDriverManager().install())


# 페이지 이동
def move(url):
    driver.get(url)
    driver.implicitly_wait(2)


# 로그인 입력
def login(id, pw):
    # 아이디 및 비밀번호 입력
    pyperclip.copy(id)
    driver.find_element(By.ID, "id").click()
    driver.find_element(By.ID, "id").send_keys(Keys.CONTROL, 'v')
    pyperclip.copy(pw)
    driver.find_element(By.ID, 'pw').click()
    driver.find_element(By.ID, 'pw').send_keys(Keys.CONTROL, 'v')
    # 로그인 클릭
    driver.find_element(By.ID, 'log.login').click()
    time.sleep(1)


# def secondLogin():
#     driver.find_element(By.ID, "useotp").click()
#     number = input()
#     pyperclip.copy(number)
#     driver.find_element(By.ID, "otp").click()
#     driver.find_element(By.ID, 'otp').send_keys(Keys.CONTROL, 'v')
#     driver.find_element(By.XPATH, '//*[@id="direct_case"]/button').click()

# 카페 검색창에 검색
def search(item):
    pyperclip.copy(item)
    search = driver.find_element(By.NAME, "query")
    search.click()
    search.send_keys(Keys.CONTROL, 'v')
    driver.find_element(By.XPATH, '//*[@id="info-search"]/form/button').click()
    driver.implicitly_wait(5)


# 로그인을 시작페이지로 정함
login_url = "https://nid.naver.com/nidlogin.login"
move(login_url)

# 로그인
login('dmswjd_14', '1q2w3e1004!')
time.sleep(5)

# 카페로 이동하기
cafe_url = 'https://cafe.naver.com/mygarden77'
move(cafe_url)

# 검색하기
search("파종시기")
