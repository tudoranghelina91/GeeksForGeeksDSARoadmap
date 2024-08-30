# Input: str = “geeksforgeeks”, chars = [1, 5, 7, 9]
# Output: g*eeks*fo*rg*eeks
# Explanation: The indices 1, 5, 7, and 9 correspond to the bold characters in “geeksforgeeks”.

# Input: str = “spacing”, chars = [0, 1, 2, 3, 4, 5, 6]
# Output: “*s*p*a*c*i*n*g”

# This works too but O(n^2) and a bit complicated = storing this in place
# str = "geeksforgeeks"
# chars = [1, 5, 7, 9]
# insertedChars = 0

# strl = list(str)

# for c in chars:
#     strl.append('#')
#     n = len(strl)
#     pos = c + insertedChars

#     for j in range(n - 1, pos, -1):
#         strl[j] = strl[j - 1]

#     strl[pos] = '*'
#     insertedChars = insertedChars + 1

# print(''.join(strl))

# This one is much simpler but takes O(n) extra space
str = "geeksforgeeks"
chars = [1, 5, 7, 9]

out = []

n = len(str)

for i in range(n):
    if i in chars:
        out.append('*')
    
    out.append(str[i])

print(''.join(out))