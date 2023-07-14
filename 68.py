# def prime_status(number):
#     divisors = [i for i in range(1, n + 1) if n % i == 0]
#     print(divisors)
#     print("prime") if len(divisors) == 2 else print("not prime")
#
#
# n = int(input("Enter any number : "))
# prime_status(n)

def prime_status(number):
    divisors = [i for i in range(1, n + 1) if n % i == 0]
    print(divisors)
    return "prime" if len(divisors) == 2 else "not prime"


n = int(input("Enter any number : "))
print(prime_status(n))
