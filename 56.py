ages = {
    "mohammad": 17,
    "arsalan": 30,
    "parinaz": 20,
    "taha": 16,
    "mina": 24
}

maxage = max(ages.values())

for i in ages:
    if ages[i] == maxage:
        print(i)
        print(maxage)
