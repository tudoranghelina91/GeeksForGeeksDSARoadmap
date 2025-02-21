def isSorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    
    return True
        
arr1 = [20, 21, 45, 89, 89, 90]
arr2 = [20, 20, 78, 98, 99, 97]

print(isSorted(arr1))
print(isSorted(arr2))