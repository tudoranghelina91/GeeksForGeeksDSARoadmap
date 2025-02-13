def duplicatesInString(s):
    occurences = {}
    for c in s:
        if c not in occurences:
            occurences[c] = 0
        occurences[c] += 1

    duplicates = {k : v for k, v in occurences.items() if v > 1}
    return duplicates

print(duplicatesInString('abcad'))