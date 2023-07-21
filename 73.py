def factorial(x):
    if x == 1:
        # return 1
        return x
    else:
        return x * factorial(x - 1)


entry = input("Number to see factorial : ")
try:
    entry = int(entry)
    # try:
    #     print(factorial(entry))
    # except RecursionError:
    #     print("Entry must be positive number")
    if entry > 0:
        print(factorial(entry))
    elif entry == 0:
        print("Factorial of zero is 1")
    else:
        print("Factorial doesnt exist")
except ValueError:
    print("Entry must be a number")
