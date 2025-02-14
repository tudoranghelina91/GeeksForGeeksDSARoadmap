def findDuplicate(arr):
    #code here
    freq = len(arr) * [False]
    
    for num in arr:
        if freq[num] == True:
            return num
        freq[num] = True

print(findDuplicate([4, 1, 3, 2, 2]))