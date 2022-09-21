
# 내장함수 : 기본적으로 제공하고 있는 함수

# abs() : 절대값
# all() : 모두 참인지 검사
    # all([1, 0, 3])
    # -> False
# chr : ASC||코드를 입력 받아서 문자로 출력함  * 0~127숫자를 각각 문자와 대응한 코드
    # chr(97)
    # -> 'a'
# dir() : 자체적으로 가지고 있는 함수를 보여줌
    # dir([1,2,3]) :리스트에서 사용될 수 있는 함수를 모두 보여줌
# divmod(분모, 분자) : 몫과 나머지를 튜플 형태로 돌려줌
    # divmod(7,3)
    # -> (2,1)
# enumeratr : "열거하다" 리스트가 있으면
# ★★★ filter : 함수를 통과하여 참인 것만 돌려줌
    # def positive():
    #   return x > 0
    #   a = list(filter(positive, [1, -3, 2, 0, -5, 6]))
    #   print(a)
    # -> [1, 2, 6]
# input() : 사용자에게 입력받는 함수
# int(), len(문자의 개수), list(리스트화 시키는 함수)
# ★★★ map() : 각 요소가 수행한 결과를 돌려줌
    # a = list(map(lambda a : a*2, [1, 2, 3, 4]))
    # print(a)
    # -> [2, 4, 6, 8]
# max(최대값 가져오기), min(최소값 가져오기)
# pow() : 제곱한 결과값 반환
    # pow(2, 4)
    # -> 16
# range(시작, 끝(미포함), 건너뛰는 간격)
# round(부동소수점) : 반올리값으로 반환
# sorted([정렬이 안된 리스트]) : 크기순으로 정렬시킴
# str(문자열로 반환시킴), tuple(튜플로 반환시킴, 문자열은 각각 나눠서)
# type(문자의 형태를 출력함)
# ★★★ zip() : 자료형을 묶어주는 역할
    # list(zip("abc", "123"))
    # -> [("a", "1"), ("b", "2"), ("c", "3")]


# <<<<< 외 장 함 수 >>>>>>>
# ★★★ pickle
# ★★★ time
    # import time
    # print(time.time())
# time.sleep(초) n초만큼 쉬면서 천천히 출력됨
# random : 난수 생성
    # import random
    # lotto = sorted(random.sample(range(1,46), 6))
    # print(lotto)
# webbrowser : 웹을 열수 있음

a = [1, 2, 3, 4]
print(a[0])