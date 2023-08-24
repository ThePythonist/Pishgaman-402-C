import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("CREATE TABLE IF NOT EXISTS students (name, age, job);")

students = [
    {"name": "sajad", "age": "22", "job": "backend dev"},
    {"name": "amir", "age": "15", "job": "db admin"},
    {"name": "sarina", "age": "16", "job": "frontend dev"},
    {"name": "elisa", "age": "16", "job": "project manager"},
    {"name": "zahra", "age": "23", "job": "frontend dev"},
    {"name": "ali", "age": "17", "job": "backend dev"},
]


def save(student):
    query = f"INSERT INTO students VALUES {(student['name'], student['age'], student['job'])};"
    cur.execute(query)
    con.commit()
    # print(f"Saved student {student['name']}")


def show():
    cur.execute("SELECT * FROM students;")
    records = cur.fetchall()
    for i in records:
        print(i)


def clear():
    cur.execute("DELETE FROM students;")


# for i in students:
#     save(i)

show()

con.commit()
con.close()
print('Done')
