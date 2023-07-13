word = "python"
indexes = {}

for i in range(len(word)):
    indexes.setdefault(word[i], i)


# count = 0
# for i in word:
#     indexes.setdefault(i, count)
#     count += 1

print(indexes)
