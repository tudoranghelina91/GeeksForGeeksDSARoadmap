def firstOccurence(txt,pat):
    #code here
    for i in range(0, len(txt) - len(pat) + 1):
        matches = 0
        for j in range(0, len(pat)):
            # print(i, j)
            if txt[i + j] == pat[j]:
                matches += 1
        
        if matches == len(pat):
            return i
    
    return -1

print(firstOccurence('abalaba', 'balaba'))