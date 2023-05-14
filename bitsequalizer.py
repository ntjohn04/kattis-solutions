PRINT = False

def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def process(S, T, b):

    swpCnt = 0

    for i in range(b):
        for j in range(b):
            if S[i] == '0' and T[i] == '1' and S[j] == '1' and T[j] == '0':
                S = swap(S, i, j)
                swpCnt += 1

    done = True
    for i in range(b):
        if S[i] != '?' and S[i] != T[i]:
            done = False

    if done == False:
        for i in range(b):
            for j in range(b):

                if S[i] == '?' and T[i] == '1' and S[j] == '1' and T[j] == '0':
                    S = swap(S, i, j)
                    swpCnt += 1

    if PRINT: print()
    if PRINT: print(S)
    if PRINT: print(T)
    if PRINT: print()

    for i in range(b):
        if S[i] == '?' or (S[i] == '0' and T[i] == '1'):
            S[i] = T[i]
            swpCnt += 1

    if S == T:
        return swpCnt
    else:
        return -1

def display(sol):
    for i, s in enumerate(sol):
        print("Case " + str(i+1) + ": " + str(s))

def main():
    C = int(input())

    sol = []
    for i in range(C):
        S = input()
        S = [*S]

        T = input()
        T = [*T]

        sol.append(process(S, T, len(T)))

    display(sol)


if __name__ == "__main__":
    main()