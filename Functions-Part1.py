def checknumber(x):
    if type(x) in [int, float]:
        print("Okay. Continue")
        return "Number"
    else:
        print("Not okay")
        return "Not Number"


# checknumber(12)


# if checknumber("python") == "Number":
#     print("Meghdar daryaft shod")
# else:
#     print("Meghdar bayad adad bashad")

# --------------------------------------------

def checknumber(x):
    if x % 2 == 0:
        print("Okay")
        return "Even"

    else:
        print("Not okay")
        return "Odd"


# if checknumber(12) == "Even":
#     print("adad zoj daryaft shode bod")

# checknumber(4)  # Call function
# print(checknumber(4))  # Print function
