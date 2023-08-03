lst=[]
f=open("words.txt").readlines()
for i in f:
    if i[-4:-1]=="ing":
        lst.append(i)
print(lst)
