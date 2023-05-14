from collections import Counter

def process(A, n, t):

    B = set(A)

    if t == 1:
        for num in B:
            if 7777-num in B:
                print("Yes")
                return
        print("No")
        return
    
    if t == 2:
        if len(A) == len(B):
            print("Unique")
            return
        else:
            print("Contains duplicate")
            return
        
    if t == 3:

        counts = Counter(A)

        #print(counts)

        k = counts.most_common()

        if k[0][1] > n/2:
            print(k[0][0])
            return
        else:
            print(-1)
            return
    
    if t == 4:
        if n % 2 == 1:
            A.sort()
            print(A[n//2])
            return
        if n % 2 == 0:
            A.sort()
            print(A[n//2-1], A[n//2])
            return
        
    if t == 5:
        A.sort()
        numbers = []

        for num in A:
            if (num >= 100):
                if num > 999:
                    break
                numbers.append(num)
                

        for i, num in enumerate(numbers):
            if i != n-1: 
                print(num, end=" ")
            else:
                print(num, end="")

def main():
    L = input()
    L = L.split(sep=' ')

    n = int(L[0])
    t = int(L[1])

    A = input()
    A = A.split(sep=' ')
    A = [int(x) for x in A]

    process(A, n, t)

if __name__ == "__main__":
    main()