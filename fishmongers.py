def process(weights, mongers):
    monies = 0
    
    weights.sort()
    mongers.sort(key=lambda x : x[1])

    A = len(weights)
    B = len(mongers)


    while A != 0 and B != 0:
        for i in range(mongers[B-1][0]):
            if A == 0:
                break
            monies += mongers[B-1][1]*weights[A-1]
            del weights[A-1]
            A -= 1
        del mongers[B-1]
        B -= 1

    return monies

def main():
    l = input()
    l = l.split()

    n = int(l[0])
    m = int(l[1])

    w = input()
    w = w.split()
    weights = []
    for we in w:
        weights.append(int(we))

    mongers = []
    for i in range(m):
        l = input()
        l = l.split()
        mongers.append([int(l[0]), int(l[1])])

    print(process(weights, mongers))


if __name__ == "__main__":
    main()