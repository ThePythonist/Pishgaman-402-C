lst=[]
f=open("words.txt").readlines()
for i in f:
    if len(i)==6:
        lst.append(i)
print(lst)
