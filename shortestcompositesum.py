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
        #print("NO")
        return False
    
    s, d = factorpow2(n-1)

    k = 1
    for i in range(k):
        a = random.randrange(2, n-2)
        x = pow(a, d, n)
        for j in range(s):
            y = pow(x, 2, n)
            if y == 1 and x != 1 and x != (n-1):
                #print("NO")
                return False
            x = y
        if y != 1:
            #print("NO")
            return False
    #print("YES")
    return True

def process(n):
    a = n//2
    if n % 2 == 1:
        b = a + 1
    else:
        b = a

    a_prime = miller_rabin(a)
    b_prime = miller_rabin(b)

    while (a_prime == True or b_prime == True):
        a -= 1
        b += 1
        a_prime = miller_rabin(a)
        b_prime = miller_rabin(b)

    print(a, b)

def main():
    n = int(input())

    print(2)
    process(n)

if __name__ == "__main__":
    main()