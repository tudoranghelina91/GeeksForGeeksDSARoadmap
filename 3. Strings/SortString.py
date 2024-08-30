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

str = "geek"
n = len(str)
# expected eegk
strl = list(str)

quickSort(strl, 0, n - 1)
print(''.join(strl))
