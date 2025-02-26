def nthTermOfAP(a1 : int, a2 : int, n : int) -> int:
    d = a2 - a1
    return (a1 + (n - 1) * d)

print(nthTermOfAP(2, 3, 4))