# lst=[]
# f=open("words.txt").readlines()[::-1]
# for i in f:
#     lst.append(i)
# output="".join(lst)
# open("baraks.txt","w").write(output)
# ------------------------------------------
lst=[]
f=open("words.txt").readlines()
for i in f:
    lst.append(i[::-1])
output="".join(lst)
open("kalamebaraks.txt","w").write(output)