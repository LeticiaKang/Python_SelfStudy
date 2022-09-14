# number를 n진수로 만들려면
# 1. number를 n으로 계속 나눠서 나머지를 모은다
# 2. 나머지가 n보다 작을 때(몫이 0이 나올 때) 멈춘다.

def make_jinsu():
    number , jinsu = map(int, input("number과 jinsu를 입력하세요.").split())
    share = 1
    remain_list = []

    check_range(number, jinsu)

    while share != 0:
        share = number // jinsu  # 20 // 3 = 6
        remain = number % jinsu  # 20 % 3 = 2
        remain_list.append(remain)      # share_list = [2, 0, 2]
        number = share

    remain_list = remain_list[::-1]

    result = ""
    for p in remain_list:
        result += str(p)

    return find_pattern(result)

def check_range(number, jinsu):
    if (number in range(0, 1000001)) == 0 or (jinsu in range(3, 11)) == 0 :
        return make_jinsu()
    else:
        pass

    # 패턴을 각각 부여할 경우 - 1개의 단어를 새로 리턴해서 찾음
    # pattern_l0 = "0[1-9]+"
    # pattern_s0 = "0[1-9]+0"
    # pattern_r0 = "[1-9]+0"
    # pattern_0 = "\s[1-9]+\s"

    # prime_l0 = re.findall(pattern_l0, result)
    # prime_s0 = re.findall(pattern_s0, result)
    # prime_r0 = re.findall(pattern_r0, result)
    # prime_0 = re.findall(pattern_0, result)
    #
    # result_prime = [prime_0, prime_r0, prime_s0, prime_l0]
    #
    # print(result, result_prime)
    # print(prime_l0)

def find_pattern(result):
    import  re
    # 패턴을 하나로 만들경우 - 단어 1개로 찾음
    pattern = "0[1-9]+|0[1-9]+0|[1-9]+0|\s[1-9]+\s"
    result_prime = []

    prime_list = re.findall(pattern, result)

    prime_list = set(prime_list)

    # for prime in prime_list:
    #     if "0" in prime:
    #         prime = prime.replace("0", "")
    #         result_prime += [prime]
    #     else:
    #         result_prime += [prime]



    # print(result, result_prime, prime_list)

    print(f"조건에 맞는 소수의 개수는 {len(prime_list)}, {prime_list}개 입니다.")

make_jinsu()




