# https://tech.kakao.com/2021/01/25/2021-kakao-recruitment-round-1/ 1번 문제

# 아이디를 입력받는다
new_id = input("아이디를 입력하세요: ")
# new_id = "abcdefghijklmn.p"
possible = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z', "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "0", "-", "_", "."]

# 2. 소문자, 숫자, 빼기, 밑줄, 마침표를 제외한 모든 문자를 제거한다.
new_id = new_id.lower()

# for ch in possible:

# 아이디를 리스트화 해서 하나 뽑는다.
for x in new_id:

    # 뽑은 문자에 대해 리스트 안에 그 문자가 있지 않다면
    if x not in possible:

        # 아이디에서 그 문자를 제거한다.
        new_id = new_id.replace(x, "")

    else:
        continue

# 3. 마침표가 2번이상 반복된 부분은 하나로 치환
while True:
    if new_id.count("..") == 0:
        break
    else:
        new_id = new_id.replace("..", ".")

while True:

    # 4. new_id에서 마침표(.)가 처음이나 끝에 위치한다면 제거
    if (new_id.endswith(".") == True) or (new_id.startswith(".") == True):
        new_id = new_id.strip(".")

    elif len(new_id) <= 2 and len(new_id) >= 0:
        # 5. new_id가 빈 문자열이라면, new_id에 "a"를 대입
        if len(new_id) == 0:
            new_id = "a"
        else:
            while len(new_id) <= 3:
                #                 print(new_id, type(new_id), len(new_id))
                new_id = new_id + new_id[len(new_id) - 1]
                break
    # 6. new_id의 길이가 16자 이상이면, new_id의 첫 15개의 문자를 제외한 나머지 문자들을 모두 제거
    elif len(new_id) > 15:
        new_id = new_id[0:15]

    else:
        break

# 예1	"...!@BaT#*..y.abcdefghijklm"	"bat.y.abcdefghi"
# 예2	"z-+.^."	"z--"
# 예3	"=.="	"aaa"
# 예4	"123_.def"	"123_.def"
# 예5	"abcdefghijklmn.p"	"abcdefghijklmn"

print(new_id)
print(len(new_id))


