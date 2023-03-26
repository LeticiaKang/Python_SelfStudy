# # 061
# # price 변수에는 날짜와 종가 정보가 저장돼 있다.
# # 날짜 정보를 제외하고 가격 정보만을 출력하라. (힌트 : 슬라이싱)
# price = ['20180728', 100, 130, 140, 150, 160, 170]
# # 출력 예시: [100, 130, 140, 150, 160, 170]
# print(price[1:])
#
# # 062
# # 슬라이싱을 사용해서 홀수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # 실행 예: [1, 3, 5, 7, 9]
# print(nums[0::2])
# print(nums[::2])
#
# # 063
# # 슬라이싱을 사용해서 짝수만 출력하라.
# nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# # 실행 예: [2, 4, 6, 8, 10]
# print(nums[1::2])
#
# # 064
# # 슬라이싱을 사용해서 리스트의 숫자를 역 방향으로 출력하라.
# nums = [1, 2, 3, 4, 5]
# # 실행 예: [5, 4, 3, 2, 1]
# print(nums[::-1])
#
# # 065
# # interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver']
# # interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# # 출력 예시: 삼성전자 Naver
# print(interest[1], interest[2])
#
# # 066 join 메서드
# # interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# # interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# # 출력 예시: 삼성전자 LG전자 Naver SK하이닉스 미래에셋대우
# interest_new = " ".join(interest)
# print(interest_new)
# # ★ 리스트를 문자열로 나타내고 싶을 때 : join
# # ★ 형태 : "요소_사이사이에_넣고_싶은_문자".join(리스트_이름)
#
# # 067 join 메서드
# # interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# # interest 리스트를 사용하여 아래와 같이 화면에 출력하라.
# # 출력 예시: 삼성전자/LG전자/Naver/SK하이닉스/미래에셋대우
# print("/".join(interest))
#
# # 068 join 메서드
# # interest 리스트에는 아래의 데이터가 바인딩되어 있다.
# # join() 메서드를 사용해서 interest 리스트를 아래와 같이 화면에 출력하라.
# # 출력 예시:
# # 삼성전자
# # LG전자
# # Naver
# # SK하이닉스
# # 미래에셋대우
# interest = ['삼성전자', 'LG전자', 'Naver', 'SK하이닉스', '미래에셋대우']
# print("\n".join(interest))
#
# # 069 문자열 split 메서드
# # 회사 이름이 슬래시 ('/')로 구분되어 하나의 문자열로 저장되어 있다.
# # 이를 interest 이름의 리스트로 분리 저장하라.
# # 실행 예시
# # >> print(interest)
# # ['삼성전자', 'LG전자', 'Naver']
# string = "삼성전자/LG전자/Naver"
# interest = string.split("/")
# print(interest)
#
# # 070 리스트 정렬
# # 리스트에 있는 값을 오름차순으로 정렬하세요.
# data = [2, 4, 3, 1, 5, 10, 9]
# print(sorted(data))  # 오름차순
# print(sorted(data,reverse=True)) # 내림차순
# # ★ sorted(리스트_이름) : 오름차순으로 정렬
#
# ======================================================================================

# # 071
# # my_variable 이름의 비어있는 튜플을 만들라.
# my_variable = ()
#
# # 072
# # 2016년 11월 영화 예매 순위 기준 top3는 다음과 같다.
# # 영화 제목을 movie_rank 이름의 튜플에 저장하라.
# # (순위 정보는 저장하지 않는다.)
# # 순위	영화
# # 1	닥터 스트레인지
# # 2	스플릿
# # 3	럭키
# movie_rank = ("닥터 스트레인지", "스플릿", "럭키키"
#
# # 073
# # 숫자 1 이 저장된 튜플을 생성하라.
# A = (1,)
# print(A, type(A))
# ★ tuple에 1개의 요소만 저장할 경우 콤마(,)를 뒤에 반드시 붙여줘야함.
#
# # 074
# # 다음 코드를 실행해보고 오류가 발생하는 원인을 설명하라.
# # >> t = (1, 2, 3)
# # >> t[0] = 'a'
# # Traceback (most recent call last):
# #   File "<pyshell#46>", line 1, in <module>
# #     t[0] = 'a'
# # TypeError: 'tuple' object does not support item assignment
# tupple은 immutable object하기 때문에 바꿀 수 없음.
#
# # ★★ 075
# # 아래와 같이 t에는 1, 2, 3, 4 데이터가 바인딩되어 있다.
# # t가 바인딩하는 데이터 타입은 무엇인가?
# t = 1, 2, 3, 4
# print(type(t))
#
# # 076
# # 변수 t에는 아래와 같은 값이 저장되어 있다.
# # 변수 t가 ('A', 'b', 'c') 튜플을 가리키도록 수정 하라.
# t = ('a', 'b', 'c')
# t = 'A', 'b', 'c'
# print(t, type(t))
#
# # 077
# # 다음 튜플을 리스트로 변환하라.
# interest = ('삼성전자', 'LG전자', 'SK Hynix')
# interest_list = list(interest)
# print(interest_list, type(interest_list))
#
# # 078
# # 다음 리스트를 튜플로 변경하라.
# interest = ['삼성전자', 'LG전자', 'SK Hynix']
# interest_tuple = tuple(interest)
# print(interest_tuple, type(interest_tuple))
#
# # 079 튜플 언팩킹
# # 다음 코드의 실행 결과를 예상하라.
# temp = ('apple', 'banana', 'cake')
# a, b, c = temp
# print(a, b, c)
#
# # 080 range 함수
# # 1 부터 99까지의 정수 중 짝수만 저장된 튜플을 생성하라.
# # (2, 4, 6, 8 ... 98)
# nums = tuple(x for x in range(2,100,2))
# nums = tuple(range(2,100,2))
# print(nums)
