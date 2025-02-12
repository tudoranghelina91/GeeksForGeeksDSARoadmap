# Return true if s is binary, else false
def isBinary(s):
    arr = list(s)
    for c in arr:
        if c != '0' and c != '1':
            return False
    
    return True

print(isBinary('001101'))
