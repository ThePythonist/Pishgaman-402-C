import random


def phone_number(operator):
    irancell_codes = random.choice(["0939", "0938", "0930", "0935"])
    hamrahaval_codes = random.choice(["0912", "0911", "0993", "0990"])
    rightell_codes = random.choice(["0921", "0922", "0923"])
    numbers = ""

    for i in range(7):
        numbers += str(random.randint(0, 9))

    if operator == 1:
        return f"{irancell_codes}{numbers}"
    elif operator == 2:
        return f"{hamrahaval_codes}{numbers}"
    elif operator == 3:
        return f"{rightell_codes}{numbers}"


for i in range(10):
    print(phone_number(3))
