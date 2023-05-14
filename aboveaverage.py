def process(S):
    S = S.split(sep=" ")
    n = int(S[0])

    S = S[1:len(S)]

    A = len(S)

    avg = 0
    for i in range(A):
        avg += int(S[i])

    avg = avg / A

    abCnt = 0
    for i in range(A):
        if int(S[i]) > avg:
            abCnt += 1

    return abCnt / n

C = int(input())

sol = []
for i in range(C):
    sol.append("{:.3f}".format(round(100*process(input()), 3)) + "%")

for s in sol:
    print(s)