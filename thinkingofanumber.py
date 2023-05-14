def process(consr):
    foo = 0
    for c in consr:
        if c[0] == "less":
            foo = 1
            break

    if foo == 0:
        return ["infinite"]

    lowest_less = 50001
    highest_high = 0
    divs = set([1])
    for c in consr:
        q = int(c[2])

        if c[0] == "less":
            if q < lowest_less:
                lowest_less = q
        
        elif c[0] == "greater":
            if q > highest_high:
                highest_high = q

        elif c[0] == "divisible":
            divs.add(q)

    sol = []
    divisiblenums = []
    for i in range(highest_high+1, lowest_less):
        notDiv = False
        for div in divs:
            if i % div != 0:
                notDiv = True
        if notDiv == False:
            divisiblenums.append(i)

    return divisiblenums

def main():
    n = int(input())

    sol = []
    while (n != 0):
        consr = []
        for i in range(n):
            l = input()
            l = l.split(sep=" ")
            consr.append(l)
        sol.append(process(consr))

        n = int(input())

    for s in sol:
        if len(s) == 0:
            print("none")

        for i, num in enumerate(s):
            if i != len(s)-1:
                print(num, end=" ")
            else:
                print(num)

if __name__ == "__main__":
    main()