# Input : s = "geeksforgeeks"
#         c = 'e'
# Output : s = "gksforgks"

# Input : s = "geeksforgeeks"
#         c = 'g'
# Output : s = "eeksforeeks"
 
# Input : s = "geeksforgeeks"
#         c = 'k'
# Output : s = "geesforgees"

s = "geeksforgeeks"
c = 'e'
aux = ''

l = list(s)
cnt = s.count(c)

while (cnt > 0):
    l.remove(c)
    cnt = cnt - 1

print(l)