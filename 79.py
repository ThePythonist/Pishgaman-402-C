factorial = lambda x: None if x < 1 else x if x == 1 else x * factorial(x - 1)
print(factorial(4))
