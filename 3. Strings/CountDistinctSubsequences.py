def verifyCurrentStep(candidateSolution, n):
    for i in range(n - 1):
        if candidateSolution[i] == candidateSolution[i + 1]:
            return False
    return True

def printOutput(str, solution):
    out = []
    n = len(solution)
    for i in range(n):
        out.append(str[solution[i]])
    print(''.join(out))

# pos = the position at which to attempt the solution
def subsequences(str, candidateSolution: list, pos: int):
    for i in range(len(str)):
        candidateSolution[pos] = i
        if verifyCurrentStep(candidateSolution, i):
            if pos == len(str):
                printOutput(candidateSolution)
            else:
                subsequences(str, candidateSolution, pos + 1)

str = "abc"
subsequences(str, [0,0,0], 0)