# Input  : arr[] = {4, 5, 6, 7, 0, 1, 2}, key = 0
# Output : 4

# Input  : arr[] = { 4, 5, 6, 7, 0, 1, 2 }, key = 3
# Output : -1

# Input : arr[] = {50, 10, 20, 30, 40}, key = 10   
# Output : 2

def binarySearch(arr, start, end):
    location = -1
    mid = (int)((start + end) / 2)

    while start <= end and mid < end:
        if key == arr[mid]:
            location = mid
            break

        if key > arr[mid]:
            start = mid + 1

        if key < arr[mid]:
            end = mid - 1
        
        mid = (int)((start + end) / 2)
    
    return location

def findPivot(arr):
    for i in range(0, n):
        if arr[i - 1] > arr[i]:
            return i

arr = [4, 5, 6, 7, 0, 1, 2]
key = 999

n = len(arr)
pivot = findPivot(arr)

location = binarySearch(arr, 0, pivot)

if location == -1:
    location = binarySearch(arr, pivot, n)

print(location)