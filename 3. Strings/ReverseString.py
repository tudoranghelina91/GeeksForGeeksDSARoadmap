str = "geeksforgeeks"
rev = []

start,end = 0,0

for i in range(len(str)-1, -1, -1):
    rev.append(str[i])

print(''.join(rev))
