# from selenium.webdriver.chrome.options import Options
# from selenium.webdriver.chrome.service import Service
# import pandas as pd #엑셀화 판다스
# from selenium.webdriver.common.action_chains import ActionChains
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys #키보드
from selenium.webdriver.common.by import By
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import pyperclip
import time

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging']) # usb에러
# options.add_argument("headless") # 브라우저 없이 실행
driver = webdriver.Chrome(options=options, executable_path=r"C:\Self_Study\PythonStudy\Project1\chromedriver")


# 로그인 함수
def login(id, pw):
    driver.get("https://nid.naver.com/nidlogin.login")
    driver.implicitly_wait(1)
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
    return print('로그인 완료')

def news_crawling(url):
    # url = 'https://media.naver.com/press/015?sid=101'
    driver.get(url)
    driver.implicitly_wait(1)

    url_list = [] # url저장 리스트
    title_list = [] # 뉴스 제목 리스트
    try:
        # 페이지의 소스를 가져와서 페이지마다 이동하는 url을 바로 저장
        soup = bs(driver.page_source, "lxml")
        links = soup.select('a.press_edit_news_link._es_pc_link') # 뉴스페이지 가져오기
        titles = soup.select('span.press_edit_news_title') # 뉴스제목 가져오기

        # 해당 태그에서 한개씩 url만 가져오기
        for link,title in zip(links, titles):
            url = link['href']
            url_list.append(url)
            title_list.append(title.text)
    except Exception as e:
        print(e)
        print("뉴스 크롤링 중 오류 발생")

    # 웹 종료
    driver.close()

    return url_list, title_list
