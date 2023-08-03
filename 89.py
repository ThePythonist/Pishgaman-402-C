lst=[]
f=open("words.txt").readlines()
for i in f:
    if i[0:3]=="sub":
        lst.append(i)
print(lst)
