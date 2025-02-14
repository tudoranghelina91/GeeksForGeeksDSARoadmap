# Input: s = “aabccccddd” 
# Output: a2b1c4d3 
# Since it is already in alphabetical order, the frequency 
# of the characters is returned for each character.

CHARS_IN_ALPHABET = 26
freq = [0] * CHARS_IN_ALPHABET # Another way to initialize the array. Insert 0 26 times

s = 'geeksforgeeks'

for c in s:
    freq[ord(c) - ord('a')] += 1

for i in range(len(freq)):
    if (freq[i] > 0):
        print(chr(i + ord('a')) + str(freq[i]), end='')

# [print(chr(i + ord('a')) + str(freq[i]), end='') for i in range(len(freq)) if freq[i] > 0]