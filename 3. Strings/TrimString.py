str = "I am     an   untr   immed      stri  ng "
newstr = []

for c in str:
    if c == " ":
        continue
    
    newstr.append(c)

newstr = ''.join(newstr)
print(newstr)

