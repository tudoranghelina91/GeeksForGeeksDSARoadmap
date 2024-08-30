arr = [7, 9, 11, 1, 5]
n = len(arr)
r = 1
k = 0

for i in range(n - 1):
    if arr[i + 1] > arr[i]:
        r = r + 1
    else:
        break
    k = k + 1

if k == n - 1:
    r = 0

print(r)

# # TODO find rotation point using binary search
# arr = [7, 9, 11, 1, 5]
# n = len(arr)
# r = 0

# start = 0
# end = n

# mid = (int)((start + end) / 2)

# while start <= end and mid < n - 1:
#     if arr[mid - 1] > arr[mid]:
#         r = mid
#         print(mid)
#         break

#     if arr[mid - 1] < arr[mid]:
#         start = mid + 1
#         mid = (int)((start + end) / 2)

# print(r)
    