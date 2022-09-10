from flask import Flask  # 플라스크를 임포트
from flask import request  # 플라스크에서 request 객체를 사용
import json 
import sqlite3

app = Flask(__name__)  # 플라스크 앱을 생성

# 데이터베이스에 연결하는 함수
def get_db_con() -> sqlite3.connect:
    return sqlite3.connect("books_db.sqlite")

#========= 모든 데이터를 내려받기 위한 hello() 함수를 정의 =========
@app.route("/")
def get_data():
    # con이라는 변수를 생d성해 데이터베이스에 접속
    with get_db_con() as con:
        cur = con.cursor()
        # hanbit_books 데이터베이스의 모든 데이터를 선택한다는 쿼리문
        q = "select * from hanbit_books"
        result = cur.execute(q)
    result_json = jsonize(result)  # 결과를 JSON 문자열로 만들어줍니다.
    return result_json

#======== 해당 url을 받아서 저자 이름을 가져올 함수를 선언 ========
# 저자 이름 요청을 받을 url을 정해줌
@app.route("/books/by/author")
def get_books_by_author():
    name = request.args.get("name")
    # 데이터베이스 커넥션을 가져와서 작업
    with get_db_con() as con:  # 작업이 끝나면 자동으로 with가 close를 호출
        cur = con.cursor()
        # 쿼리를 작성합니다. hanbit_books 테이블에서 author 컬럼이 name과 일치하는 걸 찾아옵니다.
        q = "SELECT * FROM hanbit_books WHERE author LIKE :name ORDER BY title"
        param = {"name": "%" + name + "%"}
        result = cur.execute(q, param)
    result_json = jsonize(result)
    return result_json

# ========해당 url을 받아서 출간월을 가져올 함수를 선언 =========
# 출간월 요청을 받을 url을 정해줍니다.
@app.route("/books/by/month")
def get_books_by_month():
    month = request.args.get("month")
    if int(month) < 10: # 숫자가 한 자리일 경우 앞에 "0"을 붙여줍니다.
        month = "0" + month
    with get_db_con() as con:
        cur = con.cursor()
        # 쿼리를 작성합니다. hanbit_books 테이블에서 pub_date 컬럼의 월 부분이 month와 일치하는걸 찾아옵니다.
        q = "SELECT * FROM hanbit_books WHERE strftime('%m', pub_date) = :month ORDER BY pub_date DESC"
        param = {"month": month}
        result = cur.execute(q, param)
    result_json = jsonize(result)
    return result_json

# 데이터베이스 커서의 result를 받아서 JSON 문자열로 만드는 함수
def jsonize(result):
    result_json = json.dumps(list(result.fetchall()), ensure_ascii=False).encode("utf-8")
    return result_json

if __name__ == "__main__":
    app.run(debug = True)
