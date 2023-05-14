def FirstPrimeFactor(n):
    if n & 1 == 0:
        return 2
    d= 3
    while d * d <= n:
        if n % d == 0:
            return d
        d= d + 2
    return n

def process(n):
    A = 2*n + 1

    while (FirstPrimeFactor(A) != A):
        print(A)
        A += 1

    if FirstPrimeFactor(n) != n:
        return (str(A) + " (" + str(n) + " is not prime)")
    return A
    

def main():
    n = int(input())

    answers = []
    while (n != 0):

        answers.append(process(n))

        n = int(input())

    for answer in answers:
        print(answer)


if __name__ == "__main__":
    main()