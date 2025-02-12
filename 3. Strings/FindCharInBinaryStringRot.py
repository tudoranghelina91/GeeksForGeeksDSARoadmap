# Input : m = 5, n = 2, i = 3
# Output : 1
# Input : m = 3, n = 3, i = 6
# Output : 1

m = 3
n = 3
i = 6

# Convert m to binary
mm = m
binm = []

while mm > 0:
    d = mm % 2
    binm.append(str(d))
    mm = int(mm / 2)

binm.reverse()

# Insert in place
for ii in range(n):
    for jj in range(0, len(binm), 2):
        if binm[jj] == "0":
            binm.insert(jj + 1, "1")
            continue
        
        binm.insert(jj + 1, "0")

print(binm)
print(binm[i])