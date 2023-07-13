info = {
    "name": "james",
    "age": 59,
    "instrument": "electric guitar",
    "band": "metallica",
    "city": "san fransisco"
}

key = input("Search any key : ")

# if key in info:
#     print("Found :", info[key])
# else:
#     print("Key Not Found")

try:
    print("Found :", info[key])
except KeyError:
    print("Key not found")
