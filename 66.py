# def check(word):
#     if len(set(word)) == len(word):
#         print("Tekrari nadarad")
#     else:
#         print("Tekrari darad")
#
#
# w = input("Enter any word : ")
# check(w)


def check(word):
    lst = []

    for i in word:
        if i not in lst:
            lst.append(i)
        else:
            print("Harf", i, "Tekrari ast")

    if len(lst) == len(word):
        print("Tekrari nadasht")


check("mohammad")
