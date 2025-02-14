def findTwoElements(arr): 
    freq = [0] * (len(arr) + 1)
    
    for num in arr:
        freq[num] += 1
        
    rep = 0
    missing = 0
    
    for i in range(1, len(freq)):
        if freq[i] == 2:
            rep = i
        
        if freq[i] == 0:
            missing = i

    return [rep, missing]

print(findTwoElements([1,1,3]))