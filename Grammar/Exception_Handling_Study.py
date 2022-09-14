# try:
 # 오류가 발생할 수 있는 구문

# except:
 # 오류 발생

# else:
 # 오류 발생하지 않음

# finally:
 # 무조건 마지막에 실행

try:
    4/0
except ZeroDivisionError as e:
    print(e)

print("안녕하세요")

try:
    #아래와 같이 실행시킨다.
    f = open("none", "r")
except Exception as e:
    #오류 났을 때 실행됨
    # Exception 은 최상위 오류 처리 단어
    print(str(e))
else:
    #if else처럼 위에 내용이 오류가 없을 경우 실행해라
    data = f.read()
    print(data)
    f.close()
# finally:
#     f.close()


class Bird:
    def fly(self):
        raise FileNotFoundError
    # 기존 class를 사용하되 변형을 하여 사용하게 할 때

class Eagle(Bird):
    # pass
    def fly(self):
        print("very fast")

eagle = Eagle()
eagle.fly()
