import random


def generate_number(code):
    numbers = ""
    for i in range(7):
        numbers += str(random.randint(0, 9))

    return f"{code}{numbers}"


def irancell():
    code = random.choice(["0939", "0938", "0930", "0935"])
    return generate_number(code)


def hamrahaval():
    code = random.choice(["0912", "0911", "0993", "0990"])
    return generate_number(code)


def rightell():
    code = random.choice(["0921", "0922", "0923"])
    return generate_number(code)


f = open("phonenumber.txt", "a")
for i in range(100):
    f.write(irancell() + "\n")
for i in range(100):
    f.write(hamrahaval() + "\n")
for i in range(100):
    f.write(rightell() + "\n")
