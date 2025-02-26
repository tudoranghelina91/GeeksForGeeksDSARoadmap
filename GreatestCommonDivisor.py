def gcd(a, b):
    # code here
    if b == 0:
        return a
    
    return gcd(b, a % b)

print(gcd(6, 3))