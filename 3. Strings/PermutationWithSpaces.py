def permutation(s):
    res = []
    def solve(ip, op):
        if len(ip) == 1:
            op = op + ip
            res.append(op)
            return
        
        if len(ip) > 1:
            val = ip[0]
            op1 = op[:]
            op2 = op[:]
            op1 = op1 + val
            op2 = op2 + (val + ' ')
            solve(ip[1:],op2)
            solve(ip[1:],op1)
            return
    op = ''
    solve(s,op)
    return res

print(permutation('ABC'))