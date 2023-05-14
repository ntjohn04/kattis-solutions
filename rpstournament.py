PRINT = False

def display(sol):
    if PRINT: print("DISPLAY")
    for s in sol:
        for r in s:
            if isinstance(r, str) == False:
                print("%.3f" % round(r, 3))
            else:
                print(r)

def add(di, k):
    if k not in di:
        di[k] = 0
    di[k] += 1

def process(rounds, n):
    wDict = dict()
    lDict = dict()

    for i, rnd in enumerate(rounds):


        if rnd[1] == "paper" and rnd[3] == "rock":
            add(wDict, rnd[0])
            add(lDict, rnd[2])
            
        elif rnd[1] == "paper" and rnd[3] == "scissors":
            add(wDict, rnd[2])
            add(lDict, rnd[0])
            
        elif rnd[1] == "rock" and rnd[3] == "paper":
            add(wDict, rnd[2])
            add(lDict, rnd[0])
            
        elif rnd[1] == "rock" and rnd[3] == "scissors":
            add(wDict, rnd[0])
            add(lDict, rnd[2])
            
        elif rnd[1] == "scissors" and rnd[3] == "rock":
            add(wDict, rnd[2])
            add(lDict, rnd[0])
            
        elif rnd[1] == "scissors" and rnd[3] == "paper":
            add(wDict, rnd[0])
            add(lDict, rnd[2])

        if PRINT: print(wDict)
        if PRINT: print(lDict)
        if PRINT: print()

    percs = []
    
    for i in range(1, n+1):
        if i in wDict and i in lDict:
            percs.append(wDict[i] / (wDict[i] + lDict[i]))
        elif i not in wDict and i not in lDict:
            percs.append("-")
        elif i not in wDict:
            percs.append(0.0)
        elif i not in lDict:
            percs.append(1.0)
        else:
            percs.append("-")

    percs.append("")

    return percs

def main():

    L = input()
    sol = []
    while L != '0':

        L = L.split()

        n = int(L[0])
        k = int(L[1])

        rounds = []
        for i in range(k*n*(n-1) // 2):
            G = input()
            G = G.split()

            rounds.append([int(G[0]), G[1], int(G[2]), G[3]])

        sol.append(process(rounds, n))

        L = input()

    display(sol)

if __name__ == "__main__":
    main()