PRINT = False

def getField(p):
    if p[0] % 2 == p[1] % 2:
        return 1
    else:
        return 0

def get2Moves(a, b):
    brd = [[0 for i in range(8)] for j in range(8)]

    x = b[0]
    y = b[1]
    while x < 8 and y < 8:
        brd[x][y] = 1
        x += 1
        y += 1

    x = b[0]
    y = b[1]
    while x >= 0 and y < 8:
        brd[x][y] = 1
        x -= 1
        y += 1

    x = b[0]
    y = b[1]
    while x < 8 and y >= 0:
        brd[x][y] = 1
        x += 1
        y -= 1

    x = b[0]
    y = b[1]
    while x >= 0 and y >= 0:
        brd[x][y] = 1
        x -= 1
        y -= 1

    foundLine = False
    if foundLine == False:
        x = a[0]
        y = a[1]
        while x < 8 and y < 8:
            if brd[x][y] == 1:
                foundLine = True
                break
            x += 1
            y += 1

    if foundLine == False:
        x = a[0]
        y = a[1]
        while x < 8 and y >= 0:
            if brd[x][y] == 1:
                foundLine = True
                break
            x += 1
            y -= 1

    if foundLine == False:
        x = a[0]
        y = a[1]
        while x >= 0 and y >= 0:
            if brd[x][y] == 1:
                foundLine = True
                break
            x -= 1
            y -= 1

    if foundLine == False:
        x = a[0]
        y = a[1]
        while x >= 0 and y < 8:
            if brd[x][y] == 1:
                foundLine = True
                break
            x -= 1
            y += 1
    
    if b == [x, y]:
        return [b]
    elif a == [x, y]:
        return [a, b]
    else:
        return [a, [x, y], b]

def display(sol):
    for s in sol:
        if s[0] == -1:
            print("Impossible")
            continue
    
        print(s[0], end=" ")

        for m in s[1]:
            m[1] = chr(m[1] + 65)
            print(m[1], m[0]+1, end=" ")

        print()

def process(cases):
    sol = []
    for case in cases:
        
        a = case[0]
        b = case[1]

        if PRINT: print("points a, b:", a, b)

        if a == b:
            sol.append([0, [b]])
            continue

        aF = getField(a)
        bF = getField(b)

        if PRINT: print("field comp:", aF, bF)

        if aF != bF:
            sol.append([-1])
            continue

        moves = get2Moves(a, b)

        sol.append([len(moves)-1, moves])

    return sol

def main():
    N = int(input())

    cases = []

    for i in range(N):
        L = input().split()

        a = L[:2]
        b = L[2:]

        a[0] = ord(a[0]) - 65
        b[0] = ord(b[0]) - 65

        a[1] = int(a[1]) - 1
        b[1] = int(b[1]) - 1

        a.reverse()
        b.reverse()

        cases.append([a, b])

    if PRINT: print(cases)
    if PRINT: print()
    
    sol = process(cases)

    display(sol)

if __name__ == "__main__":
    main()