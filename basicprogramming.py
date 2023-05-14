def process(A, t):
    if t == 1:
        print("7")
    elif t == 2:
        if A[0] > A[1]:
            print("Bigger")
        elif A[0] == A[1]:
            print("Equal")
        else:
            print("Smaller")
        
    elif t == 3:
        for i in range(3):
            if A[i] != min(A[:3]) and A[i] != max(A[:3]):
                print(A[i])
                break
    elif t == 4:
        s = 0
        for item in A:
            s += item
        print(s)

    elif t == 5:
        s = 0
        for item in A:
            if item % 2 == 0 and item != 0:
                s += item
        print(s)

    elif t == 6:
        for i, item in enumerate(A):

            print(chr((A[i] % 26) + 97), end="")

    elif t == 7:
        i = 0
        nodes = set()
        while True:
            i = A[i]
            if i in nodes:
                print("Cyclic")
                break

            nodes.add(i)

            if i >= len(A):
                print("Out")
                break
            elif i == len(A) - 1:
                print("Done")
                break

def main():
    L = input().split(" ")
    N = int(L[0])
    t = int(L[1])

    A = input().split(" ")
    for i in range(len(A)):
        A[i] = int(A[i])

    process(A, t)

if __name__ == "__main__":
    main()