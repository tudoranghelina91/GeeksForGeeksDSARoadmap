# Input: 10011
# Output: 10100
# Explanation:Here n = (19)10 = (10011)2
# next greater integer = (20)10 = (10100)2

# Input: 111011101001111111
# Output: 111011101010000000

input = "111011101001111111"
carry = 1

# 10011
# 00001
# -----
#   100

n = len(input)
inl = list(input)

for i in range(n - 1, 0, -1):
    
    d = int(inl[i]) + carry

    if d == 2:
        inl[i] = '0'
        carry = 1
    else:
        inl[i] = str(d)
        carry = 0

print(''.join(inl))