import random


def irancell():
    code = random.choice(["0939", "0938", "0930", "0935"])
    numbers = ""
    for i in range(7):
        numbers += str(random.randint(0, 9))

    return f"{code}{numbers}"


def hamrahaval():
    code = random.choice(["0912", "0911", "0993", "0990"])
    numbers = ""
    for i in range(7):
        numbers += str(random.randint(0, 9))

    return f"{code}{numbers}"


def rightell():
    code = random.choice(["0921", "0922", "0923"])
    numbers = ""
    for i in range(7):
        numbers += str(random.randint(0, 9))

    return f"{code}{numbers}"
