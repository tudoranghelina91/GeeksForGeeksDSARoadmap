def convertToCamelCase(s):
    # code here
    words = list(s.split(' '))
    out = []
    
    for i in range(len(words)):
        word = words[i]
        letters = list(word)
        if len(letters) == 0:
            continue
        if i > 0:
            letters[0] = letters[0].upper()
        word = ''.join(letters)
        out.append(word)
        
    return ''.join(out)

print(convertToCamelCase('ala bala portocala'))

