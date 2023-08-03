# lst=[]
# f=open("words.txt").readlines()
# for i in f:
#     if len(i)==6:
#         lst.append(i)
# print(lst)
# for i in lst:
#     open("5letters.txt","a").write(i)
#------------------------------------------------------
# fiveletters = ""
# f=open("words.txt").readlines()
# for i in f:
#     if len(i)==6:
#         fiveletters += i
# open("5letters.txt","w").write(fiveletters)
#------------------------------------------------------
fiveletters = []
f=open("words.txt").readlines()
for i in f:
    if len(i)==6:
        fiveletters.append(i)

output = "".join(fiveletters)
open("5letters.txt","w").write(output)
