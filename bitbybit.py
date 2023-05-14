def process(instr):
    N = 32
    reg = [-1]*32

    for x in instr:
        if x[0] == "SET":
            reg[int(x[1])] = 1
        
        elif x[0] == "CLEAR":
            reg[int(x[1])] = 0

        elif x[0] == "AND":
            i = int(x[1])
            j = int(x[2])

            if (reg[i] == 0 or reg[j] == 0):
                reg[i] = 0

            elif (reg[i] == 1 and reg[j] == 1):
                reg[i] = 1

            else:
                reg[i] = -1

        elif x[0] == "OR":
            i = int(x[1])
            j = int(x[2])

            if (reg[i] == 1 or reg[j] == 1):
                reg[i] = 1

            elif (reg[i] == -1 or reg[j] == -1):
                reg[i] = -1

            else:
                reg[i] = 0

    reg.reverse()
    reg = [str(x).replace("-1", "?") for x in reg]
    return reg

def main():
    n = int(input())
    sol = []
    while (n != 0):
        instr = []
        for i in range(n):
            l = input()
            l = l.split(sep=" ")
            instr.append(l)
        
        sol.append(process(instr))

        n = int(input())

    for s in sol:
        for ch in s:
            print(ch, end="")
        print()

if __name__ == "__main__":
    main()