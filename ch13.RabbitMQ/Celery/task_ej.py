from celery import Celery

# 샐러리 앱 인스턴스를 만듭니다.
app = Celery(
    # 첫 번째 파라미터는 현재 모듈의 이름입니다.
    # 이것은 작업이 __main__ 모듈 에 정의될 때 이름이 자동으로 생성될 수 있도록 하기 위해서만 필요합니다 .
    # 이 파라미터를 전달하면 현재 모듈을 단독으로 실행할 때도 문제 없도록 합니다.
    'tasks',

    # broker : 메시지 브로커의 주소 / 프로토콜과 접속 정보를 적습니다.
    # 여기서는 rabbitmq를 사용하므로, AMQP 형식의 주소를 사용했습니다.
    broker='pyamqp://guest@localhost//',

    # 결과를 저장할 backend를 지정합니다. 주로 데이터베이스를 지정합니다.
    backend="db+sqlite:///db.sqlite"
)

# @app.task 디코레이터를 붙여 이 함수가 태스크라는 것을 표시합니다.
@app.task
def add(x, y):
    return x + y

# @app.task
# def reverse(text):
#     return text[::-1]
