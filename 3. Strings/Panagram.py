#Function to check if a string is Pangram or not. Panagram means that it contains all letter of the alphabet
def checkPangram(s):
    #code here
    map = {}
    for c in range(97, 123):
        map[chr(c)] = False
        
    for c in s:
        map[c.lower()] = True

    for key in map:
        if map[key] == False:
            return False
    
    return True

print(checkPangram('Bawds jog, flick quartz, vex nymph'))