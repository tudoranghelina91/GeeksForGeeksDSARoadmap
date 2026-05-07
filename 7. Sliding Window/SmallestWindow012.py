""" 
This solution is not a sliding window, but it's easier to read and it is in O(n)
The problem can be solved easier without sliding window
We are using an occurence array. 
At the first occurence of all characters we stop and return the length
"""

def smallestWindow012(s):
    n = len(s)
    occurences = [False] * 3
    minlen = 0

    for i in range(n):
        minlen += 1

        isDigit = str(s[i]).isdigit()
        
        if (isDigit == False):
            continue
        
        charAsInt = int(s[i])

        if charAsInt in range(3):
            occurences[charAsInt] = True
            if all(occurences) == True:
                return minlen

    return -1

print(smallestWindow012("4324ABCV230123532"))