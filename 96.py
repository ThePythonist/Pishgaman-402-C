# lst=[]
# numbers=[str(i) for i in range(10)]
# f=open("words.txt").readlines()
# for i in f:
#     for j in i:
#         if j in numbers:
#             lst.append(i)
# print(lst)

lst=[]
numbers=[str(i) for i in range(10)]
alphabet = list("abcdefghijklmnopqrstuvwxyz")

f=open("words.txt").readlines()
for i in f:
    for j in i:
        if j in numbers:
            lst.append(i)

print(lst)
