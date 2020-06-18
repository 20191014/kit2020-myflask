import sqlite3
conn = sqlite3.connect('mydb.db')

# Cursor 객체 생성
c = conn.cursor()

# 데이터 불러 와서 출력
for row in c.execute('SELECT * FROM student'):
    print(row)

# 접속한 db 닫기
conn.close()

# CREATE TABLE "users" (
# 	"id"	varchar(50),
# 	"pw"	varchar(50),
# 	"name"	varchar(50),
# 	PRIMARY KEY("id")
# );