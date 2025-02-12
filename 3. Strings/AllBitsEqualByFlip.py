# Input: 101
# Output: Ye
# Explanation: In 101, the 0 can be flipped to make it all 1

# Input: 11
# Output: No
# Explanation: No matter whichever digit you flip, you will not get the desired string.

# Input: 1
# Output: Yes
# Explanation: We can flip 1, to make all 0’s

input = "111"

cnt = [0, 0]

for c in input:
    i = int(c)
    cnt[i] = cnt[i] + 1

if cnt[0] == 1 or cnt[1] == 1:
    print('Yes')
else:
    print('No')