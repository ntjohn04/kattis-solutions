def display(cases):
    for person in cases:
        print(person)
    print(30*"=")

def swap(list, pos1, pos2):
    list[pos1], list[pos2] = list[pos2], list[pos1]
    return list

def compare(p1, p2):
    i = 0
    while i < len(p1) and i < len(p2):
        if p1[i] > p2[i]:
            return 1
        elif p1[i] < p2[i]:
            return 0

        i += 1

    if len(p1) > len(p2):
        while i < len(p1):
            if p1[i] == "3":
                return 1
            elif p1[i] == "1":
                return 0
            i += 1
    else:
        while i < len(p2):
            if p2[i] == "3":
                return 0
            elif p2[i] == "1":
                return 1
            i += 1

    return -1

def solveCase(ppl):
    d = []

    di = dict()
    for l in ppl:
        ls = l.split(": ")

        tmp = ls[1].replace("middle", "2").replace("lower", "1").replace("upper", "3")[:-6]
        tmp = tmp.split("-")
        tmp.reverse()

        d.append([ls[0], tmp])

        di[ls[0]] = tmp


    sort = []
    for i, q in enumerate(d):
        sort.append(q[0])

        for j in range(len(sort) - 2, -1, -1):

            B = compare(q[1], di[sort[j]])
            if B == 1:
                pass
                #print(q[0], "classier than", sort[j])
            elif B == 0:
                #print(sort[j], "classier than", q[0])
                swap(sort, sort.index(q[0]), j)

            elif B == -1:
                #print(sort[j], "equally classy", q[0])
                if q[0] > sort[j]:
                    swap(sort, sort.index(q[0]), j)

    sort.reverse()
    return sort

def caseInput():
    n = int(input())
    ppl = []
    for i in range(n):
        ppl.append(input())

    sort = solveCase(ppl)
    return sort

def main():
    T = int(input())

    cases = []

    for i in range(T):
        cases.append(caseInput())

    for i in range(T):
        display(cases[i])

if __name__ == "__main__":
    main()