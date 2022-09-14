# # 가위, 바위, 보 업그레이드 버전 함수
# # 조건 1 : 게임을 몇 판으로 진행?
# # # 조건2 : 0,1,2, 가위, 바위,보 이외에 다른 입력을 받으면 재입력 받기
# # # 조건3 : 게입종료 후 나와 컴퓨터의 총 전적 출력
# #
# # n = int(input("게임을 몇 판으로 진행하겠습니까?"))
# # v = int(input("가위 바위 보!!(가위 = 0, 바위 = 1, 보 = 2로 입력)"))
# # if v != 0


def count_prime_number(n, m) :
    prime_count = 0
    if n < 2 :
        n = 2
    for i in range(n,m) :
        if is_prime(i) == True :
            print("소수 ok = {0}".format(i))
            prime_count = prime_count + 1

    print("소수개수 = {0}".format(prime_count))

def is_prime(number) :
    result = True
    for i in range(2,number) :
        if number % i == 0 :
            result = False
            break

    return result


# n = int(input("첫 번째 수 입력 : "))
# m = int(input("두 번째 수 입력 : "))
# count_prime_number(n,m)
count_prime_number(5, 30)