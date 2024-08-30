s = 'GeeksForGeeks'

start = 0
end = len(s) - 1
sList = list(s)

while start < end:
    sList[start], sList[end] = sList[end], sList[start]
    start = start + 1
    end = end - 1

print(''.join(sList))