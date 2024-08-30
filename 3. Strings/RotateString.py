str = 'GeeksforGeeks'

n = len(str)
r = 2

# left rotation
straux = list()
for i in range(r, n):
    straux.append(str[i])

for i in range(0, r):
    straux.append(str[i])

print(''.join(straux))

# right rotation
straux = list()
for i in range(n - r, n):
    straux.append(str[i])

for i in range(0, n - r):
    straux.append(str[i])

print(''.join(straux))
