# -*- coding: utf-8 -*-
# 플라스크를 임포트합니다.
from flask import Flask
from flask import request

# Flask 객체 선언
app = Flask(__name__)
# Flask 객체에 Api 객체 등록
app.debug = True
# URL경로에 따라 실행할 함수에 디코레이터를 사용하는데,
# 디코레이터의 파라미터가 URL의 경로가 된다.
@app.route("/")  #http://127.0.0.1:5000/
def hello():
    return "Hello World!"

@app.route("/hello")  #http://127.0.0.1:5000/hello?name=이름
def hello_to_get_param():
    name = request.args.get("name")
    return "Hello, {}!".format(name)
# /hello?name=이름 형식의 요청 받아서 '이름'을 name에 저장함

if __name__ == "__main__":
    # 위에서 생성한 플라스크 애플리케이션을 실행합니다.
    app.run()
