def sort012(arr):
    zero = 0
    one = 0
    two = 0
    # code here
    for num in arr:
        if num == 0:
            zero += 1
        if num == 1:
            one += 1
        if num == 2:
            two += 1
        
    # print(freq)
        
    out = []
    for i in range(zero):
        out.append(0)
    
    for i in range(one):
        out.append(1)
        
    for i in range(two):
        out.append(2)
        
    
    for i in range(len(arr)):
        arr[i] = out[i]

arr = [0,1,2,0,1,2]
sort012(arr)
print(arr)
