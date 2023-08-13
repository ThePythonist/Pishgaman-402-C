from random import choice, sample


def generate1(length):
    password = []
    for i in range(length):
        password.append(str(choice(range(0, 10))))

    password = "".join(password)
    print(password)


# generate1(5)

def generate2(length):
    password = [str(i) for i in sample(range(0, 10), length)]
    password = "".join(password)
    print(password)


generate2(6)
