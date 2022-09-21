# # 041 upper 메서드
# # 다음과 같은 문자열이 있을 때 이를 대문자 BTC_KRW로 변경하세요.
# ticker = "btc_krw"
# ticker_upper = ticker.upper()
# print(ticker_upper)
#
# # 042 lower 메서드
# # 다음과 같은 문자열이 있을 때 이를 소문자 btc_krw로 변경하세요.
# ticker = "BTC_KRW"
# ticker_lower = ticker.lower()
# print(ticker_lower)
#
# # 043 capitalize 메서드
# # 문자열 'hello'가 있을 때 이를 'Hello'로 변경해보세요.
# a = 'hello'
# a_capitalize = a.capitalize()
# print(a_capitalize)
#
# # 044 endswith 메서드
# # 파일 이름이 문자열로 저장되어 있을 때
# # endswith 메서드를 사용해서 파일 이름이 'xlsx'로 끝나는지 확인해보세요.
# file_name = "보고서.xlsx"
# print(file_name.endswith('xlsx'))
#
# # 045 endswith 메서드
# # 파일 이름이 문자열로 저장되어 있을 때 endswith 메서드를 사용해서
# # 파일 이름이 'xlsx' 또는 'xls'로 끝나는지 확인해보세요.
# file_name = "보고서.xlsx"
# print(file_name.endswith(("xls","xlsx")))
# # ★ 끝나는 문자는 튜플("xls","xlsx")을 이용하여 여러개 지정해줄 수 있음
#
# # 046 startswith 메서드
# # 파일 이름이 문자열로 저장되어 있을 때
# # startswith 메서드를 사용해서 파일 이름이 '2020'로 시작하는 확인
# file_name = "2020_보고서.xlsx"
# print(file_name.startswith("2020"))
#
# # 047 split 메서드
# # 다음과 같은 문자열이 있을 때 공백을 기준으로 문자열을 나눠보세요.
# a = "hello world"
# a_split = a.split()
# print(a_split)
#
# # 048 split 메서드
# # 다음과 같이 문자열이 있을 때 btc와 krw로 나눠보세요.
# ticker = "btc_krw"
# print(ticker.split("_"))
#
# # 049 split 메서드
# # 다음과 같이 날짜를 표현하는 문자열이 있을 때 연도, 월, 일로 나눠보세요.
# date = "2020-05-01"
# print(date.split("-"))
#
# # 050 rstrip 메서드
# # 문자열의 오른쪽에 공백이 있을 때 이를 제거해보세요.
# data = "039490     "
# print(data.rstrip())
# # ★ rstrip()메서드를 이용하면 기존 변수에 오른쪽 공백을 제거한 문자열을 새로 바인딩함.

#===============================================================================================

# # 051 리스트 생성
# # 2016년 11월 영화 예매 순위 기준 top3는 다음과 같습니다.
# # 영화 제목을 movie_rank 이름의 리스트에 저장해보세요.
# # (순위 정보는 저장하지 않습니다.)
# # 순위	영화
# # 1	닥터 스트레인지
# # 2	스플릿
# # 3	럭키
# movie_rank = ["닥터 스트레인지", "스플릿", "럭키"]
#
# # 052 리스트에 원소 추가
# # 051의 movie_rank 리스트에 "배트맨"을 추가하라.
# movie_rank.append("베트맨")
# print(movie_rank)
#
# # 053
# # movie_rank 리스트에는 아래와 같이 네 개의 영화 제목이 바인딩되어 있다.
# # "슈퍼맨"을 "닥터 스트레인지"와 "스플릿" 사이에 추가하라.
# movie_rank = ['닥터 스트레인지', '스플릿', '럭키', '배트맨']
# movie_rank.insert(1, "슈퍼맨")
# print(movie_rank)
# # ★ append는 맨 뒤에 추가되지만, insert(위치, 단어)는 원하는 위치에 넣을 수 있다.
#
# # 054
# # movie_rank 리스트에서 '럭키'를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '럭키', '배트맨']
# movie_rank.remove("럭키")
# print(movie_rank)
#
# # 055
# # movie_rank 리스트에서 '스플릿' 과 '배트맨'을 를 삭제하라.
# movie_rank = ['닥터 스트레인지', '슈퍼맨', '스플릿', '배트맨']
# del movie_rank[2]
# del movie_rank[2]
# print(movie_rank)
#
# # 056
# # lang1과 lang2 리스트가 있을 때 lang1과 lang2의 원소를
# # 모두 갖고 있는 langs 리스트를 만들어라.
# lang1 = ["C", "C++", "JAVA"]
# lang2 = ["Python", "Go", "C#"]
# # 실행 예:
# # >> langs
# # ['C', 'C++', 'JAVA', 'Python', 'Go', 'C#']
# langs = lang1 + lang2
# print(langs)
#
# # 057
# # 다음 리스트에서 최댓값과 최솟값을 출력하라.
# # (힌트: min(), max() 함수 사용)
# nums = [1, 2, 3, 4, 5, 6, 7]
# # 실행 예:
# # max:  7
# # min:  1
# nums_max = max(nums)
# nums_min = min(nums)
# print("max:", nums_max)
# print("min:", nums_min)
#
# # 058
# # 다음 리스트의 합을 출력하라.
# nums = [1, 2, 3, 4, 5]
# # 실행 예: 15
# print(sum(nums))
#
# # 059
# # 다음 리스트에 저장된 데이터의 개수를 화면에 구하하라.
# cook = ["피자", "김밥", "만두", "양념치킨", "족발", "피자", "김치만두", "쫄면", "소시지", "라면", "팥빙수", "김치전"]
# print(len(cook))
#
# # 060
# # 다음 리스트의 평균을 출력하라.
# nums = [1, 2, 3, 4, 5]
# # 실행 예: 3.0
# print(sum(nums)/len(nums))