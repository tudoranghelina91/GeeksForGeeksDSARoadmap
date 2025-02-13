def areAnagrams(s1, s2):
    #code here
    if (len(s1) != len(s2)):
        return False
    if (s1 == s2):
        return True
    
    # map = { 'a': 1, 'b': 3 }
    map = {}
    for c in s1:
        if c not in map:
            map[c] = 0
            
        map[c] += 1
        
    for c in s2:
        if c not in map:
            return False
        map[c] -= 1
        
    for key in map:
        if (map[key] != 0):
            return False
    
    return True

print(areAnagrams('laba', 'abal'))