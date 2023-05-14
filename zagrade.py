PRINT = False

def removeBracket(l, c):
    openCnt = 0
    closeCnt = 0

    i = 0

    while openCnt != c:
        if l[i] == "(":
            openCnt += 1
        i += 1
    openCnt = 0

    a = i-1
    while closeCnt != openCnt+1:
        if l[i] == ")":
            closeCnt += 1
        elif l[i] == "(":
            openCnt += 1
        i += 1

    b = i-1

    if PRINT: print("PERM, INDX:", c, a, b)
    l = l[:a] + l[a+1:b] + l[b+1:]
    if PRINT: print(l)
    return l

def process(p, l):
    bCnt = 0
    if PRINT: print()
    if PRINT: print("PERMUATION:", p)
    for i, b in enumerate(p):

        if b == 1:
            l = removeBracket(l, i+1-bCnt)
            bCnt += 1

    return l

def main():
    l = input()

    prs = l.count("(")

    perm = []
    for i in range(1, 2**prs):
        perm.append(tuple(map(int, bin(i)[2:].zfill(prs))))

    if PRINT: print(perm)
    sol = []
    for p in perm:
        sol.append(process(p, l))

    if PRINT: print()
    if PRINT: print(sol)

    sol.sort()
    sol = set(sol)
    for s in sol:
        print(s)

if __name__ == "__main__":
    main()