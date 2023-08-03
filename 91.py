lst=[]
f=open("words.txt").readlines()
for i in f:
    lst.append(i.replace("\n",""))
print(lst)