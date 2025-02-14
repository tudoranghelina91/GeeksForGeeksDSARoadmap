# DOES NOT APPLY FOR CAPS
# O(n * m) seems to be better than O(n log n), because (log n) will be greater than m most of the time
def sort(s): 
    MAX_CHAR = 26 # number of letters in english alphabet
    charCount = [0] * MAX_CHAR

    for ch in s:
        # ord returns the ascii code of a character. It's like casting it to an integer z = 122 a = 97
        # e.g. 122 - 97 = 25, which is the 0-based index of the last letter of the alphabet
        charCount[ord(ch) - ord('a')] += 1
    
    out = []
    
    for i in range(MAX_CHAR):
        for _ in range(charCount[i]):
            out.append(chr(i + ord('a')))
            
    return ''.join(out)

print(sort('caca'))
