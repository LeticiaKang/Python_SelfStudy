# # 201
# # "비트코인" 문자열을 화면에 출력하는 print_coin() 함수를 정의하라.
# def print_coin():
#     print("비트코인")
#
# # 202
# # 201번에서 정의한 함수를 호출하라.
# print_coin()
#
# # 203
# # 201번에서 정의한 print_coin 함수를 100번호출하라.
# for x in range(100):
#     print_coin()
#
# # 204
# # "비트코인" 문자열을 100번 화면에 출력하는 print_coins() 함수를 정의하라.
# def print_coin():
#     for x in range(101):
#         print("비트코인")
# print_coin()
#
# # 205
# # 아래의 에러가 발생하는 이유에 대해 설명하라.
# # hello()
# # def hello():
# #     print("Hi")
# # 실행 예
# # NameError: name 'hello' is not defined
# # 함수를 정의하기 전에 먼저 호출했기 때문에
#
# # 206
# # 아래 코드의 실행 결과를 예측하라.
# # def message() :
# #     print("A")
# #     print("B")
# # message()
# # print("C")
# # message()
#
# # 207
# # 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# # print("A")
# # def message() :
# #     print("B")
# # print("C")
# # message()
# # A C B
#
# # 208
# # 아래 코드의 실행 결과를 예측하라. (읽기 어려운 코드의 예입니다.)
# # print("A")
# # def message1() :
# #     print("B")
# # print("C")
# # def message2() :
# #     print("D")
# # message1()
# # print("E")
# # message2()
# # A C B E D
#
# # 209
# # 아래 코드의 실행 결과를 예측하라.
# #
# # def message1():
# #     print("A")
# #
# # def message2():
# #     print("B")
# #     message1()
# #
# # message2()
# # B A
#
# # 210
# # 아래 코드의 실행 결과를 예측하라.
# #
# # def message1():
# #     print("A")
# #
# # def message2():
# #     print("B")
# #
# # def message3():
# #     for i in range (3) :
# #         message2()
# #         print("C")
# #     message1()
# #
# # message3()
# # B C B C B C A

# =================================================

# # 211
# # 함수의 호출 결과를 예측하라.
# #
# # def 함수(문자열) :
# #     print(문자열)
# #
# # 함수("안녕")
# # 함수("Hi")
# # 안녕
# # Hi
# #
# # 212
# # 함수의 호출 결과를 예측하라.
# #
# # def 함수(a, b) :
# #     print(a + b)
# #
# # 함수(3, 4)
# # 함수(7, 8)
# # 7
# # 15
# #
# # 213
# # 아래와 같은 에러가 발생하는 원인을 설명하라.
# #
# # def 함수(문자열) :
# #     print(문자열)
# # 함수()
# # TypeError: 함수() missing 1 required positional argument: '문자열'
# #
# #
# # 214
# # 아래와 같은 에러가 발생하는 원인을 설명하라.
# #
# # def 함수(a, b) :
# #     print(a + b)
# #
# # 함수("안녕", 3)
# # TypeError: must be str, not int
# # 숫자와 문자열은 더할 수 없기 때문에에
# #
# # 215
# # 하나의 문자를 입력받아 문자열 끝에 ":D" 스마일 문자열을 이어 붙여 출력하는 print_with_smile 함수를 정의하라.
# string = input("입력해봐.")
def print_with_smile(a):
    print( a + ":D")
print_with_smile("string")

# # 216
# # 215에서 정의한 함수를 호출하라. 파라미터는 "안녕하세요"로 입력하라.
# string = input("입력해봐.")
# def print_with_smile(string):
#     print( string + ":D")
# print_with_smile(string)
#
# # 217
# # 현재 가격을 입력 받아 상한가 (30%)를 출력하는 print_upper_price 함수를 정의하라.
# price = int(input("현재 가격을 입력하세요. \n"))
# def print_upper_price():
#     print(price * 1.3)
# print_upper_price()
#
# # 218
# # 두 개의 숫자를 입력받아 두 수의 합을 출력하는 print_sum 함수를 정의하라.
# num_1 = int(input("num_1 = "))
# num_2 = int(input("num_2 = "))
# def print_sum():
#     print("num_1 + num_2 =", num_1 + num_2)
# print_sum()
#
# # 219
# # 두 개의 숫자를 입력받아 합/차/곱/나눗셈을 출력하는 print_arithmetic_operation 함수를 작성하라.
# num_1 = int(input("num_1 = "))
# num_2 = int(input("num_2 = "))
# def print_arithmetic_operation():
#     print(f"{num_1} + {num_2} =", num_1 + num_2)
#     print(f"{num_1} - {num_2} =",  num_1 - num_2)
#     print(f"{num_1} / {num_2} =",  num_1 / num_2)
#     print(f"{num_1} * {num_2} =",  num_1 * num_2)
# print_arithmetic_operation()
