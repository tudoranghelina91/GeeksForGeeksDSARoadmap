# Dutch National Flag - Very good algorithm to sort arrays with 3 distinct values
def sort012DNF(arr):
    low, mid, high = 0, 0, len(arr)  - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
sort012DNF(arr)
print(arr)