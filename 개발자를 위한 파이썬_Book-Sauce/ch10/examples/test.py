import sqlite3

# 데이터베이스 파일이 저장될 경로와 파일 이름을 써서 데이터베이스에 접속합니다.
con = sqlite3.connect("C:/Py_Study/ch10/examples/db.sqlite")

# 유니코드 인코딩 문제가 발생하면 해당 코드의 주석을 해제하고 실행하세요.
# con.text_factory = str

# 메모리에서 직접 데이터베이스를 이용하는 코드입니다.
# con = sqlite3.connect(":memory:")

# 데이터베이스를 동작시키기 위한 Cursor 객체를 생성합니다.
# 데이터베이스를 사용하기 위한 마지막 준비라고 생각하면 됩니다.
cur = con.cursor()

# 이제 무언가 하면 됩니다.
# cur.execute("""create table hanbit_books_2 (
#                title varchar(100),
#                author varchar(100),
#                translator varchar(100),
#                pub_date date,
#                isbn varchar(100)
#            )""")
con.commit()

cur.execute("insert into hanbit_books values (?, ?, ?, ?, ?)", ("책 이름", "저자 이름", "번역자 이름", "2016-08-22"," 9788968480011"))

query_str = "insert into hanbit_books values (:title, :title, :title, :pub_date, :isbn)"
params = {
    "title":"책 이름",
    "pub_date":"2017-10-12",
    "isbn":9788968480022
}

cur.execute(query_str, params)


import csv

# csv 파일을 엽니다.
csv_file = open("C:\\Py_Study\\ch10\\examples\\book_list.csv", encoding='utf-8')

# 연 파일을 csv 리더로 읽습니다.
# csv_reader = open("C:\\Py_Study\\ch10\\examples\\book_list.csv", 'r', encoding='utf-8')
csv_reader = csv.reader(csv_file)

# csv 파일을 list 형식으로 바꿉니다.
book_list = list(csv_reader)

# csv header를 제거합니다.
book_list = book_list[1:]

# 최초 크롤링할 때 있었던 저자 혹은 번역자 데이터의 앞뒤 공백을 제거합니다.
for item in book_list:
    item[1] = item[1].strip()
    item[2] = item[2].strip()

# 제대로 되었나 출력해봅니다.
print("■■■■■■■■■■■■■■■■■■■■book_list■■■■■■■■■■■■■■■■■■■■■■\n", book_list)

cur.executemany("insert into hanbit_books values (?, ?, ?, ?, ?)", book_list)

con.commit()

cur.execute("select * from hanbit_books where author = ?", ("윤웅식",))
print("■■■■■■■■■■■■■■■■cur.fetchone()■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(cur.fetchone())

query_str = "select * from hanbit_books where author=:name"
params = {"name":"윤인성"}

cur.execute(query_str, params)

result = list(cur.fetchall())

for row in result:
    print(row)

query_str = "update hanbit_books set isbn =:isbn where author=:name"
params = {
    "isbn":9788968480033,
    "name":"윤웅식"
}

cur.execute(query_str, params)

cur.execute("select * from hanbit_books where author = ?",("윤웅식",))
print("■■■■■■■■■■■■■■■■cur.fetchone()■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(cur.fetchone())

cur.execute("delete from hanbit_books where author = ?",("윤웅식",))

cur.execute("select * from hanbit_books where author = ?",("윤웅식",))
print("■■■■■■■■■■■■■■■■cur.fetchone()■■■■■■■■■■■■■■■■■■■■■■■■■■■■■")
print(cur.fetchone())

# 테이블 삭제
cur.execute("drop table hanbit_books")

# 데이터베이스 접속 종료
con.close()