from collections import defaultdict

def countDistinct(arr, k):
    # Code here

    # We count the occurences of elements in the first window.
    # We then proceed with the elements starting from the second window. 
    # Starting from the second window and up until the end, we decrement from the occurences of the previous window

    n = len(arr)
    res = []
    freq = defaultdict(int)
    
    for i in range(k):
        freq[arr[i]] += 1
        
    res.append(len(freq))
    
    for i in range(k, n):
        freq[arr[i]] += 1
        freq[arr[i - k]] -= 1
        
        if freq[arr[i - k]] == 0:
            del freq[arr[i - k]]
            
        res.append(len(freq))
    
    return res

arr = [1, 2, 1, 3, 4, 2, 3]
k = 4

print(countDistinct(arr, 4))