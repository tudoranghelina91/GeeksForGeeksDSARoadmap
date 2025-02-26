def countSetBits(n):
    # code here
    cnt = 0
    while n > 0:
        if n % 2 == 1:
            cnt += 1
            
        n = int(n / 2)
        
    return cnt

print(countSetBits(6))