#Inneficient

def maxOfSubarrays(self, arr, k):
    # code here
    out = []
    
    for i in range(len(arr) - k + 1):
        maxi = arr[i]
        for j in range(i + 1, i + k):
            maxi = max(maxi, arr[j])
        
        out.append(maxi)
        
    return out