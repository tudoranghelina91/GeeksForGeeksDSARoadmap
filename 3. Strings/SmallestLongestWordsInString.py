chars = "GeeksforGeeks A Computer Science portal for Geeks"

words = chars.split(" ")

minword = words[0]
maxword = words[0]

for word in words:
    if len(word) < len(minword):
        minword = word
    if len(word) > len(maxword):
        maxword = word

print(minword)
print(maxword)