# # 021 문자열 인덱싱
# # letters가 바인딩하는 문자열에서 첫번째와 세번째 문자를 출력하세요.
# # >> letters = 'python'
# # 실행 예 : p t
# letters = 'python'
# print(letters[0], letters[2])
#
# # 022 문자열 슬라이싱
# # 자동차 번호가 다음과 같을 때 뒤에 4자리만 출력하세요.
# # >> license_plate = "24가 2210"
# # 실행 예: 2210
# license_plate = "24가 2210"
# print(license_plate[4:8])
# print(license_plate[-4:])
#
# # 023 문자열 인덱싱
# # 아래의 문자열에서 '홀' 만 출력하세요.
# # >> string = "홀짝홀짝홀짝"
# # 실행 예 : 홀홀홀
# string = "홀짝홀짝홀짝"
# print(string[::2])
#
# # 024 문자열 슬라이싱
# # 문자열을 거꾸로 뒤집어 출력하세요.
# # >> string = "PYTHON"
# # 실행 예: NOHTYP
# string = "PYTHON"
# print(string[::-1])
# # ★ 문자열 거꾸로 출력하는 방법
# #  문자열 슬라이싱 이용 : 변수명[::-1]
# #  전체의 문자열에 대해 뒤에서 부터 1개씩 출력하겠다는 의미
#
# # 025 문자열 치환
# # 아래의 전화번호에서 하이푼 ('-')을 제거하고 출력하세요.
# # >> phone_number = "010-1111-2222"
# # 실행 예 : 010 1111 2222
# phone_number = "010-1111-2222"
# phone_number_new = phone_number.replace("-", " ")
# print(phone_number_new)
# # ★ 문자열 치환 : 변수.replace("기존 문자열" , "바꾸고 싶은 문자역", 횟수)
#
# # 026 문자열 다루기
# # 25번 문제의 전화번호를 아래와 같이 모두 붙여 출력하세요.
# # 실행 예 : 01011112222
# print(phone_number.replace("-", ""))
#
# # 027 문자열 다루기
# # url 에 저장된 웹 페이지 주소에서 도메인을 출력하세요.
# # >> url = "http://sharebook.kr"
# # 실행 예 : kr
# url = "http://sharebook.kr"
# print(url[-2::])
# print(url.split(".")[-1])
#
# # 028 문자열은 immutable
# # 아래 코드의 실행 결과를 예상해보세요.
# # >> lang = 'python'
# # >> lang[0] = 'P'
# # >> print(lang)
# lang = 'python'
# lang[0] = 'P'
# print(lang)
# # ★ 문자열은 인덱스로 특정 부분을 바꿀 수 없는 immutable성질을 가짐
#
# # lang029 replace 메서드
# # 아래 문자열에서 소문자 'a'를 대문자 'A'로 변경하세요.
# # >> string = 'abcdfe2a354a32a'
# # 실행 예 : Abcdfe2A354A32A
# string = 'abcdfe2a354a32a'
# string_new = string.replace("a", "A")
# print(string_new)
#
# # 030 replace 메서드
# # 아래 코드의 실행 결과를 예상해보세요.
# # >> string = 'abcd'
# # >> string.replace('b', 'B')
# # >> print(string)
# string = 'abcd'
# string.replace('b', 'B')
# print(string)
# # ★ 문자열은 immutable하기 때문에 replace함수를 사용해서 기존 변수에 영향을 주지 않음

# =======================================================================================================================

# # 031 문자열 합치기
# # 아래 코드의 실행 결과를 예상해보세요.
# # >> a = "3"
# # >> b = "4"
# # >> print(a + b)
# 34
# #
# # 032 문자열 곱하기
# # 아래 코드의 실행 결과를 예상해보세요.
# # >> print("Hi" * 3)
# HiHiHi
#
# # 033 문자열 곱하기
# # 화면에 '-'를 80개 출력하세요.
# # 실행 예:
# # --------------------------------------------------------------------------------
# print("-" * 80)
#
# # 034 문자열 곱하기
# # 변수에 다음과 같은 문자열이 바인딩되어 있습니다.
# # >>> t1 = 'python'
# # >>> t2 = 'java'
# # 변수에 문자열 더하기와 문자열 곱하기를 사용해서 아래와 같이 출력해보세요.
# # 실행 예 : python java python java python java python java
# t1 = 'python'
# t2 = 'java'
# print((t1 + " " + t2 + " ") * 4)
#
# # 035 문자열 출력
# # 변수에 다음과 같이 문자열과 정수가 바인딩되어 있을 때 % formatting을 사용해서 다음과 같이 출력해보세요.
# name1 = "김민수"
# age1 = 10
# name2 = "이철희"
# age2 = 13
# # 이름: 김민수 나이: 10
# # 이름: 이철희 나이: 13
# print("이름: %s  나이: %d" %(name1, age1))
# print("이름: %s  나이: %d" %(name2, age2))
#
# # 036 문자열 출력
# # 문자열의 format( ) 메서드를 사용해서 035번 문제를 다시 풀어보세요.
# print("이름: {0}  나이: {1}".format(name1, age1))
# print("이름: {0}  나이: {1}".format(name2, age2))
#
# # 037 문자열 출력
# # 파이썬 3.6부터 지원하는 f-string을 사용해서 035번 문제를 다시 풀어보세요.
# print(f"이름: {name1}  나이: {age1}")
# print(f"이름: {name2}  나이: {age2}")
#
# # 038 컴마 제거하기
# # 삼성전자의 상장주식수가 다음과 같습니다. 컴마를 제거한 후 이를 정수 타입으로 변환해보세요.
# 상장주식수 = "5,969,782,550"
# 상장주식수_1 = int(상장주식수.replace(",", ""))
# print(상장주식수_1, type(상장주식수_1))
#
# # 039 문자열 슬라이싱
# # 다음과 같은 문자열에서 '2020/03'만 출력하세요.
# 분기 = "2020/03(E) (IFRS연결)"
# print(분기[:7])
#
# # 040 strip 메서드
# # 문자열의 좌우의 공백이 있을 때 이를 제거해보세요.
# data = "   삼성전자    "
# data_1 = data.strip()
# print(data_1)