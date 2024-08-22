s = "geeksforgeeks"
p = "for"
found = False

for i in range(0, len(s) - len(p)):
    cnt = 0
    for j in range(0, len(p)):
        if p[j] == s[i + j]:
            cnt += 1
    if cnt == len(p):
        print(F"{p} found in {s} at index {i}")
        found = True
        break

if not found:
    print(F"{p} not found in {s}")