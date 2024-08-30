def partition(str, start, end):
    pivot = str[end]
    i = start - 1

    for j in range(start, end + 1):
        if str[j] < pivot:
            i = i + 1
            str[i], str[j] = str[j], str[i]
    i = i + 1

    str[i], str[end] = str[end], str[i]
    return i

def quickSort(str, start, end):
    if end <= start:
        return
    
    pivot = partition(str, start, end)
    quickSort(str, start, pivot - 1)
    quickSort(str, pivot + 1, end)

# Input: str = “geeksforgeeks” 
# Output: e4f1g2k2o1r1s2 

str = "geeksforgeeks"
dict = {}

for c in str:
    if c in dict:
        dict[c] = dict[c] + 1
        continue
    dict[c] = 1

# sortedKeys = sorted(dict)
keys = list(dict.keys())
quickSort(keys, 0, len(keys) - 1)

s = list()

for key in keys:
    s.append("{}{}".format(key, dict[key]))

print(''.join(s))