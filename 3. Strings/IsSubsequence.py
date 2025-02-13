# Subsequence means that chars are present in provided order
def isSubSequence(A, B):
    #code here
    cnt = 0
    start = 0
    for i in range(0, len(A)):
        for j in range(start, len(B)):
            if A[i] == B[j]:
                cnt += 1
                start = j + 1
                break
                
        if cnt == len(A):
            return 1
    
    return 0

print(isSubSequence("l", "la"))