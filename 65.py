def printnumbers(x, y):
    numbers = range(x, y)
    # print(list(numbers))

    # newnumbers = [*numbers]
    # print(newnumbers)

    print(*numbers)


printnumbers(50, 60)
