def reverseString(str, i = 0):
    n = len(str)
    
    # // = floor division (returns the integer part)
    # / = normal division (will return float)

    if i == n // 2:
        return
    
    str[i], str[n - i - 1] = str[n - i - 1], str[i]
    reverseString(str, i + 1)

str = list('GeeksForGeeks')
reverseString(str)
print(''.join(str))