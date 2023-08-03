f = open("words.txt").readlines()
lst = []
for i in f:
    try:
        i = int(i)
        lst.append(i)
    except ValueError:
        # print("addad nist")
        pass
print(lst)
