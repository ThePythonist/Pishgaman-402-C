def numbertype(x): # Pasokh darad
    if x % 2 == 0:
        return "Even"
    else:
        return "Odd"


def checknumber(x):  # Pasokh nadarad
    if type(x) in [int, float]:
        print("X is a number")
        print("X is", numbertype(x))
    else:
        print("X is not a number")


checknumber("Something")
