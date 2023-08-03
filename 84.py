def f1(text):
    text = text.split()
    lengths = [len(i) for i in text]
    for i in text:
        if len(i) == max(lengths):
            return i

txt = "i love python programming language"
# print(f1(txt))

def f2(text):
    text = text.split()
    text.sort(key=len)
    return text

# print(f2(txt))
def f3(text):
    text = text.split()
    return max(text,key=len)
print(f3(txt))
