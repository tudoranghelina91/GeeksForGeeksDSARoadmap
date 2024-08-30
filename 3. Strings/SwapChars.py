# Input : S = "ABCDEFGH", B = 4, C = 3;
# Output:  DEFGBCAH

# Input : S = "ABCDE", B = 10, C = 6;
# Output : ADEBC

S = "ABCDE"
B = 10
C = 6
N = len(S)

K = B
s = list(S)

for i in range(B):
    if K > 0:
        s[i], s[(i + C) % N] = s[(i + C) % N], s[i]
        # print(''.join(s)) - # Debug

print(''.join(s))
    
#TODO FIX THIS
    