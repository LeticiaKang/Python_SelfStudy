import sqlite3

# 데이터베이스에 접속 "파일경로/파일이름.확장자"
con = sqlite3.connect("C:/Py_Study/self_study/PythonStudy/books_db.sqlite")

# 데이터베이스를 동작시키기 위한 Cursor 객체를 생성(명령을 실행하기 위한 엔터라고 생각하면 됨)
cur = con.cursor()

# <테이블 생성하기 : create table 테이블명 (컬럼명1 타입, 컬럼명2 타입, … )>
cur.execute("""create table hanbit_books (
               title varchar(100),
               author varchar(100),
               translator varchar(100),
               pub_date date,
               isbn varchar(100))
           """)
con.commit()

import csv
# csv 파일을 열기 : open("파일경로/파일명.확장자", "r", encoding = 'utf-8')
csv_file = open("C:/Py_Study/self_study/PythonStudy/ScrapyTest/hanbit_crawling/book_list.csv"
, 'r',encoding= 'utf-8')
# csv파일 읽기
csv_reader = csv.reader(csv_file)
# csv 파일을 list 형식으로 바꿈
book_list = list(csv_reader)
# csv header를 제거
book_list = book_list[1:]
# 최초 크롤링할 때 있었던 저자 혹은 번역자 데이터의 앞뒤 공백을 제거
for item in book_list:
    item[1] = item[1].strip()
    item[2] = item[2].strip()
# 출력
print(book_list)  

<csv를 db에 넣기 : executemany>
cur.executemany("insert into hanbit_books values (?, ?, ?, ?, ?)", book_list)
con.commit()

# <원하는 데이터 추가하기(1개) : insert into 테이블명 values 원하는 값>
cur.execute("insert into hanbit_books values (?, ?, ?, ?, ?)", ("책 이름1", "이인제", "", "2016-08-22"," 231243213123"))
query_str = "insert into hanbit_books values (:title, :author, :translator, :pub_date, :isbn)"
params = {
    "title":"책 이름3",
    "author":"이인제",
    "translator":"",    
    "pub_date":"2017-10-12",
    "isbn":9788968480022
}
cur.execute(query_str, params)
con.commit()


# <원하는 조건으로 데이터 출력하는 방법 2가지 : select * from 테이블명 where 조건>
cur.execute("select * from hanbit_books where author = ?", ("이인제",))
print(cur.fetchone())

query_str = "select * from hanbit_books where author=:name"
params = {"name":"이인제"}
cur.execute(query_str, params)

result = list(cur.fetchall())  # 전체 데이터를 한번에 가져와
# result = list(cur.fetchmany(size=1))  # 1회만 돌려서 가져와

for row in result:
    print(row)

# <원하는 조건의 데이터 수정하기 : update 테이블명 set 변경값 where 조건>
query_str = "update hanbit_books set isbn =:isbn where author=:name"
params = {
    "isbn":123456799999,
    "name":"박상현"
}

cur.execute(query_str, params)
con.commit()

# <원하는 조건으로 데이터 삭제하기 : delete from 테이블명 where 조건>
cur.execute("delete from hanbit_books where author = ?",("윤웅식",))


# <테이블 삭제하기 : drop table 테이블명>
cur.execute("drop table hanbit_books_test")

# <데이터베이스 접속 종료>
con.close()
