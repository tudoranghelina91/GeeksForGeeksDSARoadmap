s = "geeksforgeeks"
p = "for"
r = "plm"

foundIndex = -1

for i in range(0, len(s) - len(p)):
    cnt = 0
    for j in range(0, len(p)):
        if s[i + j] == p[j]:
            cnt += 1
    
    if cnt == len(p):
        foundIndex = i
        break

if foundIndex >= 0:
    x = list(s)
    k = 0
    for i in range(foundIndex, foundIndex + len(p)):
        x[i] = r[k]
        k += 1
    s = ''.join(x)

print(s)