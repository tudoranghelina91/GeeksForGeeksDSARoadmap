str = "geeks"

def subSequence(str, n):
    out = []
    for i in range(0, len(str)):
        for j in range(i, n):
            out.append(str[i])
    print(out)

for i in range(1, len(str) + 1):
    subSequence(str, i)

