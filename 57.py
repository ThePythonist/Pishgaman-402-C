scores = {
    "riazi1": 17,
    "mabani computer": 20,
    "madar haye manteghi": 16,
    "zaban omomi": 18,
    "fizik1": 9,
    "andishe eslami": 13
}

# SUM = 0
#
# for k, v in scores.items():
#     SUM += v
#
#     if v >= 10:
#         print(k, ": Passed")
#     else:
#         print(k, ": Failed")
#
# moadel = SUM / len(scores)
# print(moadel)

# ---------------------------------------------

for k, v in scores.items():

    if v >= 10:
        print(k, ": Passed")
    else:
        print(k, ": Failed")

moadel = sum(scores.values()) / len(scores)
print(moadel)
