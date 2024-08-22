def performAllRotations(str, start):
    str1 = []
    if start == len(str):
        return
    for i in range(start, len(str)):
        str1.append(str[i])
    for i in range(0, start):
        str1.append(str[i])
    
    if str1 not in list:
        list.append(''.join(str1))

    performAllRotations(str, start + 1)

str = "geeks"
list = []

performAllRotations(str, 0)
print(list)