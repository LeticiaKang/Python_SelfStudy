# # 221
# # 입력된 문자열을 역순으로 출력하는 print_reverse 함수를 정의하라.
# # print_reverse("python")
# # nohtyp
# def print_reverse(name):
#     name_reverse = name[::-1]
#     print(name_reverse)
# print_reverse("python")
#
# # 222
# # 성적 리스트를 입력 받아 평균을 출력하는 print_score 함수를 정의하라.
# # print_score ([1, 2, 3]) : 2.0
# def print_score(a):
#     print(sum(a) / 3)
# print_score ([1, 2, 3])
#
# # 223
# # 하나의 리스트를 입력받아 짝수만 화면에 출력하는 print_even 함수를 정의하라.
# # print_even ([1, 3, 2, 10, 12, 11, 15])
# # 2
# # 10
# # 12
# def print_even(a):
#     for x in range(len(a)):
#         if a[x] % 2 == 0:
#             print(a[x])
#         else:
#             continue
# print_even ([1, 3, 2, 10, 12, 11, 15])
#
# # 224
# # 하나의 딕셔너리를 입력받아 딕셔너리의 key 값을 화면에 출력하는 print_keys 함수를 정의하라.
# # print_keys ({"이름":"김말똥", "나이":30, "성별":0})
# # 이름
# # 나이
# # 성별
# def print_keys_1(a):
#     a_keys = list(a.keys())
#     for x in range(len(a_keys)):
#         print(list(a.keys())[x])
#
# def print_keys_2(a):
#     for x in a.keys():
#         print(x)
#
# print("1")
# print_keys_1({"이름": "김말똥", "나이": 30, "성별": 0})
# print("2")
# print_keys_2({"이름": "김말똥", "나이": 30, "성별": 0})
#
# # 225
# # my_dict에는 날짜를 키값으로 OHLC가 리스트로 저장돼 있다.
# my_dict = {"10/26" : [100, 130, 100, 100],
#            "10/27" : [10, 12, 10, 11]}
# # my_dict와 날짜 키값을 입력받아 OHLC 리스트를 출력하는 print_value_by_key 함수를 정의하라.
# # print_value_by_key  (my_dict, "10/26")
# # [100, 130, 100, 100]
# def print_value_by_key(dict_name, key_name):
#     print(dict_name[key_name])
# print_value_by_key  (my_dict, "10/26")
#
# # 226
# # 입력 문자열을 한 줄에 다섯글자씩 출력하는 print_5xn(string) 함수를 작성하라.
# # print_5xn("아이엠어보이유알어걸")
# # 아이엠어보
# # 이유알어걸
# def print_5xn(input_string):
#     a = int(len(input_string) / 5)
#     for x in range(a+1):
#         print( input_string [ 5*x : 5*(x+1) ] )
# print_5xn("아이엠어보이유알어걸여기부터")
#
# # 227
# # 문자열과 한줄에 출력될 글자 수를 입력을 받아 한 줄에 입력된 글자 수만큼 출력하는 print_mxn(string) 함수를 작성하라.
# # print_mxn("아이엠어보이유알어걸", 3)
# # 아이엠
# # 어보이
# # 유알어
# # 걸
# def print_mxn(string, num):
#     string_chunk = int(len(string)/num)
#     for x in range(string_chunk+1):
#         print(string[num*x : num*(x+1)])
# print_mxn("아이엠어보이유알어걸", 3)
#
# # 228
# # 연봉을 입력받아 월급을 계산하는 calc_monthly_salary(annual_salary) 함수를 정의하라. 회사는 연봉을 12개월로 나누어 분할 지급하며, 이 때 1원 미만은 버림한다.
# # calc_monthly_salary(12000000)
# # 1000000
# def calc_monthly_salary(annual_salary):
#     print(annual_salary//12)
#
# calc_monthly_salary(12000000)
#
# # 229
# # 아래 코드의 실행 결과를 예측하라.
# # def my_print (a, b) :
# #     print("왼쪽:", a)
# #     print("오른쪽:", b)
# # my_print(a=100, b=200)
# # 왼쪽: 100
# # 오른쪽: 200
#
# # 230
# # 아래 코드의 실행 결과를 예측하라.
# # def my_print (a, b) :
# #     print("왼쪽:", a)
# #     print("오른쪽:", b)
# # my_print(b=100, a=200)
# # 왼쪽: 200
# # 오른쪽: 100

# # ===============================================================================

# # 231
# # 아래 코드를 실행한 결과를 예상하라.
# # def n_plus_1 (n) :
# #     result = n + 1
# # n_plus_1(3)
# # print (result)
# # 리턴값이 없어서 에러가 남 & 함수내 정의된 result는 함수 밖에서 출력되지 않음
#
# # 232
# # 문자열 하나를 입력받아 인터넷 주소를 반환하는 make_url 함수를 정의하라.
# # make_url("naver")
# # www.naver.com
# def make_url(site_name):
#     print("www." + site_name + ".com")
# make_url("naver")
#
# # 233
# # 문자열을 입력받아 각 문자들로 구성된 리스트로 반환하는 make_list 함수를 정의하라.
# # make_list("abcd")
# # ['a', 'b', 'c', 'd']
# def make_list(name):
#     print(list(name))
# make_list("abcdefg")
#
# # 234
# # 숫자로 구성된 하나의 리스트를 입력받아, 짝수들을 추출하여 리스트로 반환하는 pickup_even 함수를 구현하라.
# # pickup_even([3, 4, 5, 6, 7, 8])
# # [4, 6, 8]
# def pickup_even(input_list):
#     even_list = []
#     for x in input_list:
#         if x % 2 == 0:
#             even_list.append(x)
#     return even_list
#
# pickup_even([3, 4, 5, 6, 7, 8])
# print(pickup_even([3, 4, 5, 6, 7, 8]))
#
# # 235
# # 콤마가 포함된 문자열 숫자를 입력받아 정수로 변환하는 convert_int 함수를 정의하라.
# # convert_int("1,234,567")
# # 1234567
# def convert_int(somthing):
#     change = int(somthing.replace(",", ""))
#     return change
# print(convert_int("1,234,567"))
#
# # 236
# # 아래 코드의 실행 결과를 예측하라.
# # def 함수(num) :
# #     return num + 4
# # a = 함수(10)
# # b = 함수(a)
# # c = 함수(b)
# # print(c)
# # 14
# # 18
# # 22
# # 22
#
# # 237
# # 아래 코드의 실행 결과를 예측하라.
# # def 함수(num) :
# #     return num + 4
# # c = 함수(함수(함수(10)))
# # print(c)
# # 22
#
# # 238
# # 아래 코드의 실행 결과를 예측하라.
# # def 함수1(num) :
# #     return num + 4
# # def 함수2(num) :
# #     return num * 10
# # a = 함수1(10)
# # c = 함수2(a)
# # print(c)
# # 140
#
# # 239
# # 아래 코드의 실행 결과를 예측하라.
# # def 함수1(num) :
# #     return num + 4
# # def 함수2(num) :
# #     num = num + 2
# #     return 함수1(num)
# # c = 함수2(10)
# # print(c)
# # 16
#
# # 240
# # 아래 코드의 실행 결과를 예측하라.
# # def 함수0(num) :
# #     return num * 2
# # def 함수1(num) :
# #     return 함수0(num + 2)
# # def 함수2(num) :
# #     num = num + 10
# #     return 함수1(num)
# # c = 함수2(2)
# # print(c)
# # 28
#
# ==========================================
#
# # 241 현재시간
# # datetime 모듈을 사용해서 현재 시간을 화면에 출력해보세요.
# import datetime
# print(datetime.datetime.now())
#
# # 242 현재시간의 타입
# # datetime 모듈의 now 함수의 리턴 값의 타입을 화면에 출력해보세요.
# import datetime
# now = datetime.datetime.now()
# print(now, type(now))
#
# # 243 timedelta ????
# # datetime 모듈의 timedelta를 사용해서 오늘로부터 5일, 4일, 3일, 2일, 1일 전의 날짜를 화면에 출력해보세요.
# import datetime
#
# now = datetime.datetime.now()
#
# for day in range(5, 0, -1):
#     delta = datetime.timedelta(days=day)
#     date = now - delta
#     print(date)
#
#
# # 244 strftime
# # 현재시간을 얻어온 후 다음과 같은 포맷으로 시간을 출력해보세요. strftime 메서드를 사용하세요.
# # 18:35:01
# import datetime
# now = datetime.datetime.now()
# print(now.strftime("%H:%M:%S"))
#
# # 245 strptime
# # datetime.datetime.strptime 메서드를 사용하면 문자열 형식의 시간을 datetime.datetime 타입의 시간 값으로 만들어줍니다.
# # "2020-05-04"의 문자열을 시간 타입으로 변환해보세요.
# import datetime
#
# now = "2020-05-04"
# now_time = datetime.datetime.strptime(now, "%Y-%m-%d")
# print(now_time, type(now_time))
#
# # 246 sleep 함수
# # time 모듈, datetime 모듈을 사용해서 1초에 한 번 현재 시간을 출력하는 코드를 작성하세요.
# import datetime
# import time
#
# while True:
#     now = datetime.datetime.now()
#     print(now)
#     time.sleep(1)
#
# 247 모듈 임포트
# 모듈을 임포트하는 4가지 방식에 대해 설명해보세요.
#
# # 248 os 모듈
# # os 모듈의 getcwd 함수를 호출하여 현재 디렉터리의 경로를 화면에 출력해보세요.
# import os
# a = os.getcwd()
# print(a, type(a))
#
# # 249 rename 함수
# # 바탕화면에 텍스트 파일을 하나 생성한 후 os 모듈의 rename 함수를 호출하여 해당 파일의 이름을 변경해보세요.
# import os
# os.rename("C:/Users/USER/Desktop/This_is_test.txt", "C:/Users/USER/Desktop/This_is_change_name.txt")
#
# # 250 numpy
# # numpy 모듈의 arange 함수를 사용해서 0.0 부터 5.0까지 0.1씩 증가하는 값을 화면에 출력해보세요.
# import numpy
# for x in numpy.arange(0, 5, 0.1):
#     print(x)