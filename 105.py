import jdatetime

now = str(jdatetime.datetime.now()).split()
date = now[0]
time = now[1]

print(date)
print(time[:5])
