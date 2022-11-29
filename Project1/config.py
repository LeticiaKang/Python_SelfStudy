import configparser

# 1. 선언
config = configparser.ConfigParser()

# 2.파일 읽기
config.read(['QT.py'])
# 2-1. 한글이 들어갈 경우 오류 방지를 위해 인코딩
config.read('config.ini', encoding='cp949')

# 3.파일 저장
with open('example.ini', 'w') as configfile: # with : 파일 열고 닫음
    config.write(configfile)

