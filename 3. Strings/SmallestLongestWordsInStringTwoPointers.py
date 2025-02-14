chars = "GeeksforGeeks A Computer Science portal for Geeks"

i = 0
j = 0

# extract first word
k = 0
wordlist = []

while (k < len(chars) and chars[k] != ' '):
    wordlist.append(chars[k])
    k += 1

maxword = ''.join(wordlist)
minword = ''.join(wordlist)

while i < len(chars):
    word = []
    while j < len(chars) and chars[j] != ' ':
        word.append(chars[j])
        j += 1

    if len(word) > len(maxword):
        maxword = ''.join(word)
    if len(word) < len(minword):
        minword = ''.join(word)

    i = j + 1
    j = i

print(minword)
print(maxword)