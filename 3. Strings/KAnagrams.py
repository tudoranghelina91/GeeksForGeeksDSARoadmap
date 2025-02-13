def areKAnagrams(s1, s2, k):
    # code here
    if len(s1) != len(s2):
        return False
    
    map = {}
    
    for c in s1:
        if c not in map:
            map[c] = 0
        
        map[c] += 1
        
    for c in s2:
        if c in map and map[c] > 0:
            map[c] -= 1
        
    cnt = sum(map.values())
    
    if cnt > k:
        return False
    return True

print(areKAnagrams('fodr', 'gork', 2))