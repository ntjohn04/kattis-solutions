def process(l, A, B):
    A.sort()
    B.sort(reverse=True)

    c = 0
    for i in range(l):
        c += A[i]*B[i]

    return c

def main():
    n = int(input())

    sol = []
    for i in range(n):
        l = int(input())
        A = input()
        A = A.split(sep=" ")
        A = [int(x) for x in A]
        B = input()
        B = B.split(sep=" ")
        B = [int(x) for x in B]

        sol.append(process(l, A, B))

    for i, s in enumerate(sol):
        print("Case #" + str(i+1) + ": " + str(s))

if __name__ == "__main__":
    main()