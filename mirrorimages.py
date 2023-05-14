import copy

def process(B, r, c):
    A = copy.deepcopy(B)

    for i in range(r):
        A[i] = B[r-1-i][::-1]

    return A

def main():
    T = int(input())

    sol = []
    for i in range(T):

        L = input()
        L = L.split(sep=" ")
        r = int(L[0])
        c = int(L[1])
        
        B = []
        for i in range(r):
            B.append(input())

        sol.append(process(B, r, c))

    for i, s in enumerate(sol):
        print("Test " + str(i+1))
        for q in s:
            print(q)

if __name__ == "__main__":
    main()