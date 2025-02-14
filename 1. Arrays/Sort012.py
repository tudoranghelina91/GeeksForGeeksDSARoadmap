def sort012(arr):
    # code here
    freq = [0] * 3
    
    for num in arr:
        freq[num] += 1
        
    # print(freq)
        
    out = []
    for i in range(len(freq)):
        if freq[i] > 0:
            for j in range(freq[i]):
                out.append(i)
    
    for i in range(len(out)):
        arr[i] = out[i]

arr = [0,1,2,0,1,2]
sort012(arr)
print(arr)
