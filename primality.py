import random

def factorpow2(a):
    b = a
    i = 1
    a //= 2
    while (a % 2 == 0):
        a //= 2
        i += 1

    return i, (b // (2 ** i))

def miller_rabin(n):
    if n % 2 == 0:
        print("NO")
        return
    
    s, d = factorpow2(n-1)

    k = 1
    for i in range(k):
        a = random.randrange(2, n-2)
        x = pow(a, d, n)
        for j in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != (n-1):
                print("NO")
                return
            x = y
        if y != 1:
            print("NO")
            return
    print("YES")
    return


def main():
    n = int(input())

    if n in [2, 3]:
        print("YES")
        return
    
    miller_rabin(n)

if __name__ == "__main__":
    main()