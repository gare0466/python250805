# db1.py
import sqlite3

#연결객체를 리턴
con = sqlite3.connect(r"c:\work\sample.db")  # 메모리 내 데이터베이스 생성
cur = con.cursor()  # 커서 객체 생성
#테이블 생성
cur.execute("CREATE TABLE Phonebook (name TEXT, phone text);")
#데이터 삽입
cur.execute("INSERT INTO Phonebook values ('Alice', '123-4567')")
name = '이순신'
phone = '987-6543' 
cur.execute("INSERT INTO Phonebook values (?,?);", (name, phone))
# 여러건 입력 
datalist = (("김길동", "010-111"), ("박영희", "010-2222"), ("홍길동", "010-3333"))
cur.executemany("INSERT INTO Phonebook values (?,?);", datalist)

#데이터 조회
cur.execute("SELECT * FROM Phonebook")
for row in cur:
	print(row)
#작업을 정상적으로 종료
con.commit()
