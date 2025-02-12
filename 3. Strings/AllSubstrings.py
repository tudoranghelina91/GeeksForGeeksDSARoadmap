# Input :  abcd
# Output :  a 
#           b
#           c
#           d
#           ab
#           bc
#           cd
#           abc
#           bcd
#           abcd

input = "abcd"
n = len(input)

# i = end so far (0 to n)
for i in range(1, n + 1):
    # j = solutions made up of number of n - i + 1 letters
    for j in range(n - i + 1):
        out = []
        # k = generate solution of length i starting from j
        for k in range(j, j + i):
            out.append(input[k])
        print(''.join(out))
