# # Q1. 세자리마다 ,를 찍어주는 함수 만들기
def make_comma(숫자):
    숫자 = int(숫자)
    result = f"{숫자:,}"
    print(result)

make_comma(1000000)

# # Q2 특정 글자가 몇 개 있는지 궁금
import pandas as pd

a = """안녕하세요
반갑습니다. 파이썬 공부는 정말 재밌습니다."""

with open("생성.txt", "a", encoding = "UTF-8") as file:
    file.write(a)

def count_word(a, word):
    count_number = a.count(word)
    return count_number

print(count_word(a, "습니다"))

# # Q3 잘못되 형식으로 전화번호를 쓴 사람 찾아내는 함수
# guest_book = """
# 김갑,123456789
# 이을,010-1234-5678
# 박병,010-5678-111
# 최정,111-1111-1111
# 정무,010-3333-3333
# """
#
# def wrong_guest_book(book):
#
#     import re
#     guest_object = re.compile("(?P<name>^\w+)[,](?P<number>\d+[-]\d+[-]\d+|\d+)", re.M)
#     # guest_object = re.compile("^\w+[,]\d+[-]\d+[-]\d+", re.M)
#     m = guest_object.findall(book)
#
#     for x in range(0,4):
#         if len(m[x][1]) != 13 :
#             이름 = m[x][0]
#             번호 = m[x][1]
#
#             print(f"""잘못 쓴 사람: {이름}
# 잘못 쓴 번호: {번호}\n""")
#
# print(wrong_guest_book(guest_book))
#
#
#
#
# # print(guest_book)






# with open("all_guest_book.txt", "a", encoding = "UTF-8") as file:
#     file.write(guest_book)
#
# def wrong_guest_book(guest_book):
#     count_number = guest_book.count(word)
#     return count_number
#
# wrong_guest_book(guest_book)

# Q4. 주민번호를 입력하면 몇년 몇월 생인지 그리고 남자인지 여자인지
# 주민번호는 6자리, -로 구분 -> 만족안하면 "잘못된 번호입니다"출력
# 1,3은 남자, 2,4는 여자
# 00~21로 시작할 경우 2000년 이후 출생자인지 물어볼 것
# 3,4를 가질 수 있는 사람은 00년생 이후 출생자 밖에 없음

def check_if():
    while True:
        a = input("주민번호를 입력하세요. \na = ")
        hypen = a.find("-")
        year = a[0:2]
        month = a[2:4]

        # print(len(a), hypen)

        if len(a) != 14 or hypen == -1 or hypen != 6:  # 14자리가 아니라면 또는 하이픈이 없는 경우
            print("잘못된 번호입니다.\n올바른 번호를 넣어주세요.")

        elif len(a) == 14 & hypen == 6:  # 입력한 번호가 14자리 맞는 경우
            if int(a[0:1]) >= 0 and int(a[0:1]) <= 21:  # 00~21 사이 수로 시작하는 경우
                answer = input("2000년 이후 출생자 입니까? 맞으면 o 아니면x : ")

                if answer == "o":
                    if a[hypen+1] in [1,3]:
                        print(f"{year}년{month}월 남자")
                    elif a[hypen+1] in [2,4]:
                        print(f"{year}년{month}월 여자")

                elif answer == "x":
                    if a[hypen + 1] in [1, 2]:
                        if a[hypen + 1] == 1:
                            print(f"{year}년{month}월 남자")
                        else:
                            print(f"{year}년{month}월 여자")
                    elif a[hypen + 1] not in [1, 2]:
                        print("잘못된 번호입니다. 주민번호 또는 답변을 확인하세요.")

                else:
                    print("o 또는 x로 다시 입력하세요!")

            # if generation(a) == 1:
            #     if int(a[hypen + 1]) in [1, 3]:
            #         print(f"{year}년{month}월 남자")
            #     elif int(a[hypen + 1]) in [2, 4]:
            #         print(f"{year}년{month}월 여자")
            # else:
            #     if int(a[hypen + 1]) == 1:
            #         print(f"{year}년{month}월 남자")
            #     elif int(a[hypen + 1]) == 2:
            #         print(f"{year}년{month}월 여자")
            #

# 500512-1234567
        # else:
        #     print("잘못된 번호입니다.\n올바른 번호를 넣어주세요.")

# def generation(a):
#     if int(a[0:1]) >= 0 and int(a[0:1]) <= 21: #00~21 사이 수로 시작하는 경우
#         genr = input("2000년 이후 출생자 입니까? 맞으면 o 아니면x : ")
#         if genr == "o":
#             return True
#         elif genr == "x":
#             # print("잘못된 번호입니다. 주민번호 앞자리를 확인하세요.")
#             return False
#         else:
#             print("o 또는 x로 다시 입력하세요!")
#             return check_if()
    # else:
    #     if int(a[hypen + 1]) == 1 or 3:
    #         print(f"{year}년{month}월 남자")
    #     elif int(a[hypen + 1]) == 2 or 4:
    #         print(f"{year}년{month}월 여자")
    #     else:
    #         print("잘못된 번호입니다.\n 주민번호 앞자리를 확인해주세요.")

check_if()
# generation("500512-1234567")