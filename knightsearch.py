fav = "ICPCASIASG"
fav2 = "ICPASG"

PRINT = False

def subProc(b, i, j, n, q):

    if PRINT: print(n, "nnn")
    if PRINT: print(fav[q])

    if q == 9:
        return True

    if i + 2 < n and j + 1 < n:
        
        if b[i+2][j+1] == fav[q+1]:
            if PRINT: print("checking", i+2, j+1, "- value is -", b[i+2][j+1])
            if subProc(b, i+2, j+1, n, q+1):
                return True

    if i + 2 < n and j - 1 >= 0:

        if b[i+2][j-1] == fav[q+1]:
            if PRINT: print("checking", i+2, j-1, "- value is -", b[i+2][j-1])
            if subProc(b, i+2, j-1, n, q+1):
                return True

    if i + 1 < n and j + 2 < n:

        if b[i+1][j+2] == fav[q+1]:
            if PRINT: print("checkinasdg", i+1, j+2, "- value is -", b[i+1][j+2])
            if subProc(b, i+1, j+2, n, q+1):
                return True
    
    if i + 1 < n and j - 2 >= 0:

        if b[i+1][j-2] == fav[q+1]:
            if PRINT: print("checking", i+1, j-2, "- value is -", b[i+1][j-2])
            if subProc(b, i+1, j-2, n, q+1):
                return True

    if i - 2 >= 0 and j + 1 < n:

        if b[i-2][j+1] == fav[q+1]:
            if PRINT: print("checking", i-2, j+1, "- value is -", b[i-2][j+1])
            if subProc(b, i-2, j+1, n, q+1):
                return True

    if i - 2 >= 0 and j - 1 >= 0:
    
        if b[i-2][j-1] == fav[q+1]:
            if PRINT: print("checking", i-2, j-1, "- value is -", b[i-2][j-1])
            if subProc(b, i-2, j-1, n, q+1):
                return True

    if i - 1 >= 0 and j + 2 < n:
    
        if b[i-1][j+2] == fav[q+1]:
            if subProc(b, i-1, j+2, n, q+1):
                if PRINT: print("checking", i-1, j+2, "- value is -", b[i-1][j+2])
                return True

    if i - 1 >= 0 and j - 2 >= 0:
        
        if b[i-1][j-2] == fav[q+1]:
            if PRINT: print("checking", i-1, j-2, "- value is -", b[i-1][j-2])
            if subProc(b, i-1, j-2, n, q+1):
                return True

def process(n, b, l):
    if n >= 3:

        if n == 3:
            b[1][1] = "?"
            l[4] = "?"
            if PRINT: print(l)


        possible = False
        for i in range(n):
            for j in range(n):
                if possible == False and b[i][j] == 'I':
                    if subProc(b, i, j, n, 0):
                        return True

    return False

def main():
    n = int(input())
    L = input()

    l = [*L]

    if PRINT: print(l)

    b = []

    for i in range(n):
        b.append(l[i*n:(i+1)*n])

    if PRINT: print()

    if PRINT: print(b)

    res = process(n, b, l)

    if res == True:
        print("YES")
    else:
        print("NO")

if __name__ == "__main__":
    main()