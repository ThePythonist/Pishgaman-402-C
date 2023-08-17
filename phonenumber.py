import random


def generate_number(code):
    numbers = ""
    for i in range(7):
        numbers += str(random.randint(0, 9))

    return f"{code}{numbers}"


def irancell():
    code = random.choice(["0939", "0938", "0930", "0935"])
    print(generate_number(code))


def hamrahaval():
    code = random.choice(["0912", "0911", "0993", "0990"])
    print(generate_number(code))


def rightell():
    code = random.choice(["0921", "0922", "0923"])
    print(generate_number(code))


if __name__ == "__main__":
    print("You are using this code as a script")
    irancell()
    hamrahaval()
    rightell()
else:
    print("You are using this code as module")
