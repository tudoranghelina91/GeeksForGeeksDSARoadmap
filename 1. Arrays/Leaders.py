def leaders(arr):
    # code here
    out = [arr[len(arr) - 1]]
    
    for i in range(len(arr) - 2, -1, -1):
        if arr[i] >= out[len(out) - 1]:
            out.append(arr[i])

    out.reverse()
    return out

print(leaders([61,61,17]))