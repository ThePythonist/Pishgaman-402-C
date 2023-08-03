def f1():
    f=open("words.txt").readlines()
    f.sort(key=len)
    print(f[-1])
    print(len(f[-1]))
    print(f[0])
    print(len(f[0]))

def f2():
    f=open("words.txt").readlines()
    longest = max(f,key=len)
    print(longest)
    print(len(longest))

def f3():
    f = open("words.txt").readlines()
    longest = max(f, key=len)
    for i in f:
     if len(i)==len(longest):
        print(i)
# f1()
# print("----------------------")
# f2()
# print("----------------------")
f3()