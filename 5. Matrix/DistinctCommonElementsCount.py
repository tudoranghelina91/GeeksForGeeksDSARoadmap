def distinct(M, N):
    # code here
    map = {}
    
    for i in range(N):
        for j in range(N):
            if M[i][j] not in map:
                map[M[i][j]] = []
                
            if i not in map[M[i][j]]:
                map[M[i][j]].append(i)

    cnt = 0
    
    for key, val in map.items():
        # print(key, val)
        if len(val) == N:
            cnt += 1
            
    return cnt


N = 4
M = [[2, 1, 4, 3],
     [1, 2, 3, 2],
     [3, 6, 2, 3],
     [5, 2, 5, 3]]

print(distinct())