lst=[]
f=open("words.txt").readlines()
for i in f:
    lst.append(i.replace("\n",""))
output="".join(lst)
open("1kaht.txt","w").write(output)
