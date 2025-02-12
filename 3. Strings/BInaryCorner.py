# Combinari de n luate cate k

def binarySubstring(n,s):  
    numberOf1s = 0
    for c in s:
        if c == '1':
            numberOf1s += 1
    
    nf = 1
    for i in range(1, numberOf1s + 1):
        nf *= i
    
    kf = 2
    nk = numberOf1s - kf
    nkf = 1
    
    for i in range(1, nk + 1):
        nkf *= i
    
    return int(nf / (kf * nkf))

count = binarySubstring(5, '11111')
print(count)