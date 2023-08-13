from random import sample
from time import sleep


def generate(length):
    password = [str(i) for i in sample(range(0, 10), length)]
    password = "".join(password)
    print(password)


generate(6)

counter = 0
time_left = 60 # Can be changed to any number

while True:
    counter += 1
    sleep(1)
    if counter == time_left:
        generate(6)
        counter = 0
