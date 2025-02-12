# Input : 00011110001110
# Output : 2
# We need to convert 1's sequence
# so string consist of all 0's.
# Input : 010101100011
# Output : 4

# Count the number of groups of 0s and 1s and return the smallest number

str = "0101011000110"

lstr = list(str)
n = len(str)

cnt = [0, 0]

if lstr[0] != lstr[n - 1]:
    ctoint = int(lstr[n - 1])
    cnt[ctoint] = cnt[ctoint] + 1

for i in range(n - 1):
    if lstr[i + 1] != lstr[i]:
        ctoint = int(lstr[i])
        cnt[ctoint] = cnt[ctoint] + 1

print(min(cnt))
    