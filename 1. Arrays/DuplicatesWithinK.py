    def checkDuplicatesWithinK(self, arr, k):
        for i in range(len(arr)):
            subset = arr[i+1:i+k+1]
            if arr[i] in subset:
                return True
        return False