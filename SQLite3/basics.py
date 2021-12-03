import sqlite3 as sql

connection=sql.connect("DB1.db")
crsr=connection.cursor()

crsr.execute("SELECT * FROM Student")
# store all the fetched data in the ans variable
ans= crsr.fetchall()
# loop to print all the data
for i in ans:
    print(i)

connection.commit()
connection.close()