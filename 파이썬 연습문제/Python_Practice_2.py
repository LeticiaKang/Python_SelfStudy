# # 예제 1
# def GuGu(number):
#     x = 1
#     result = []
#     while x < 10:
#         result.append(number * x)
#         x += 1
#     return result
#
# print(GuGu(2))

#예제 2 : 1~1000까지의 합 구하기
# result = 0
# # check =[]
# for n in range(1,1000):
#     if n % 3 == 0 or n % 5 == 0:
#         # check.append(n)
#         result += n
# print(result)
# # print(check)


# #예제 3 : 게시판 페이징하기
# # 게시물의 총 건수와 한 페이지에 보여줄 게시물 수를 입력으로 주었을 때
# # 총 페이지수를 출력하는 프로그램
#
# # m = int(input("게시물의 총 건수 : "))
# # n = int(input("한 페이지에 보여줄 게시물의 수 : "))
# # def GetTotalPage():
# #     if m % n == 0:
# #         result = m//n
# #     else:
# #         result = m//n + 1
# #     return result
# #
# # print(GetTotalPage())
#
# # 홀수만 출력
# # 50이하만 출력
# # 8단 입력
# # number = int(input("몇 단? : "))
# # x = 1
# #
# # def gugudan(number):
# #     for x in range(100):
# #         x += 1
# #         result = number * x
# #         if x % 2 == 0 or result > 50:
# #             pass
# #         else:
# #             print("{} X {} = {}".format(number, x, result))
# #     return
# #
# # gugudan(number)
#
# # 가위, 바위, 보 업그레이드 버전 함수
# # 조건 1 : 게임을 몇 판으로 진행?
# # # 조건2 : 0,1,2, 가위, 바위,보 이외에 다른 입력을 받으면 재입력 받기
# # # 조건3 : 게입종료 후 나와 컴퓨터의 총 전적 출력
# #
# # n = int(input("게임을 몇 판으로 진행하겠습니까?"))
# # v = int(input("가위 바위 보!!(가위 = 0, 바위 = 1, 보 = 2로 입력)"))
# # if v != 0
#
#
# # Q3. 2개의 숫자를 입력하여 그 사이에 짝수만 출력하는 함수를 만들어 봅시다. 그리고 중앙값도 함께 출력 해봅시다.
# # (단, 중앙값이 짝수가 아닐 경우에는 중앙값은 출력을 하지 않고, 짝수인 수만 출력한다)
# # 중앙값: 정중앙에 있는 값
# # 특정 두 숫자 사이의 수들을 리스트로 만드는 법
# #
# # n = int(input("첫 번째 수 입력 : "))
# # m = int(input("두 번째 수 입력 : "))
# # numbers = [ 2*i for i in range(n,(m//2+1))]  # 2의 배수로 구성
# # mid = numbers[len(numbers)//2 ]   #중앙값
# #
# # if len(numbers) % 2 == 1:  #리스트안 요소들의 개수가 홀수일 경우
# #     print("{}과 {} 사이의 중앙값은 {} 입니다.".format(n, m, mid))
# # else: #개수가 짝수인 경우 중앙값을 구하지 않음
# #     print("중앙값이 없습니다.")
# #
# # print(numbers, "개수 : ", len(numbers))
#
# ==============================================================
#
# 문제 4. 2개의 숫자를 입력, 그 사이에 소수가 몇 개인지 출력하는 함수
# 입력
# n = int(input("첫 번째 수 입력 : "))
# m = int(input("두 번째 수 입력 : "))
# count_prime_number(n, m)
#
# 출력
# 소수 개수  4
#
# n = int(input("첫 번째 수 입력 : "))
# m = int(input("두 번째 수 입력 : "))
# def count_prime_number(n, m):
#     result = []
#     for x in range(n,m):
#         if x == 1:
#             continue
#         elif x > 1:
#             for i in range(2, x):
#                 if x % i == 0:
#                     break
#             else:
#                 result.append(x)
#                 print("{}는 소수입니다.".format(x))
#     return("소수의 개수 {}개 입니다.".format(len(result)))
#
# print(count_prime_number(n,m))

#
# ==============================================================
#
# 문제 4. 2개의 숫자를 입력, 그 사이에 소수가 몇 개인지 출력하는 함수
# 입력
# n = int(input("첫 번째 수 입력 : "))
# m = int(input("두 번째 수 입력 : "))
# count_prime_number(n, m)
# 출력 : 소수 개수  4
#
# n = int(input("첫 번째 수 입력 : "))
# m = int(input("두 번째 수 입력 : "))

# def count_prime_number(n, m):
#     prime = []
#     for x in range(n, m+1):
#         if x <= 1:
#             continue
#         else:
#             for i in range(2, x):
#                 if x % i == 0:
#                     break
#             else:
#                 prime.append(x)
#                 print(f"{x}는 소수입니다.")
#
#     print(f"소수개수 : {len(prime)}")
#
# count_prime_number(1, 10)
#
#=========================================================================
# 약수 와 약수개수 구하기
num = int(input("입력한 수: "))
divisor_list = []
def divisor(num):
    for x in range(1, num+1):
        if num % x == 0:
            divisor_list.append(x)
            print(f"{x} : 약수ㅇ")
    else:
        print(f"약수의 개수 : {len(divisor_list)}")

divisor(num)