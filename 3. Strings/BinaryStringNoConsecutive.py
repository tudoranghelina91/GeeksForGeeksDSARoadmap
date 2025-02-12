# Input : K = 3  
# Output : 000 , 001 , 010 , 100 , 101 

# Input : K  = 4 
# Output :0000 0001 0010 0100 0101 1000 1001 1010

# TODO: IMPLEMENT

def verify(solution):
    n = len(solution)
    for i in range(n - 1):
        if solution[i] == "1" and solution[i + 1] == "1":
            return False
    return True

# Generate indices of positions to place 1
def generate(arr, k, i):
    if k == i:
        isValid = verify(arr)
        if isValid:
            print(''.join(arr))
        return

    arr[i] = "0"
    generate(arr, k, i + 1)
    arr[i] = "1"
    generate(arr, k, i + 1)

n = 20
arr = [None] * n
generate(arr, n, 0)
        