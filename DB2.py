import sqlite3

con = sqlite3.connect('info.db')
cur = con.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS employees(
id INTEGER PRIMARY KEY,
name VARCHAR(50),
code INT,
job VARCHAR(70)
);
""")

students = [
    {"name": "Sajad", "code": "40211", "job": "Backend Developer"},
    {"name": "Amir", "code": "40212", "job": "Frontend Developer"},
    {"name": "Sarina", "code": "40213", "job": "Security Engineer"},
    {"name": "Zahra", "code": "40214", "job": "DevOps Engineer"},
    {"name": "Elisa", "code": "40215", "job": "Civil Engineer"},
]


def save(student):
    query = f"INSERT INTO employees(name,code,job) VALUES {(student['name'], student['code'], student['job'])};"
    cur.execute(query)
    con.commit()


# for i in students:
#     save(i)

# cur.execute(f"INSERT INTO employees(name,code,job) VALUES ('Ahora','40223','Project Manager')")

# cur.execute("SELECT * FROM employees WHERE id=4;")
cur.execute("SELECT * FROM employees;")
records = cur.fetchall()

for i in records:
    print(i)

# print(records)

con.commit()
con.close()
print('Done')
