import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

student = {"name": "Pedram", "code": 40414, "job": "Devops Engineer"}
student = tuple(student.values())

cur.execute("SELECT * FROM employees;")
records = cur.fetchall()


# for i in records:
#     print(i)

# cur.execute("DELETE FROM employees;")

def save():
    query = f"INSERT INTO employees(name,code,job) VALUES {(student[0], student[1], student[2])};"
    cur.execute(query)


users = [i[1:] for i in records]
# print(users)
# for i in users :
#     print(i)
#
if student in users:
    print("User already exists in db")
else:
    save()
    print("User added to database")

cur.execute("SELECT * FROM employees;")
records = cur.fetchall()
for i in records:
    print(i)

print(len(records), "Users exist in db")

con.commit()
con.close()
