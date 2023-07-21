check = lambda word: "Tekrari nadarad" if len(set(word)) == len(word) else "Tekrari darad"
print(check("hi"))