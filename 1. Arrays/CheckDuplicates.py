def checkDuplicates(arr):
    #code here
    occurences = []
    for num in arr:
        if num in occurences:
            return True
        occurences.append(num)
    return False

print(checkDuplicates([3, 5, 3, 12, 2, 19]))