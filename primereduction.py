import itertools

def prime_factors(n):
    f = 2
    increments = itertools.chain([1,2,2], itertools.cycle([4,2,4,2,4,6,2,6]))
    for incr in increments:
        if f*f > n:
            break
        while n % f == 0:
            yield f
            n //= f
        f += incr
    if n > 1:
        yield n

def process(n, i):
    facts = list(prime_factors(n))

    if len(facts) == 1:
        return [n, i]

    return process(sum(facts), i+1)

def main():
    n = int(input())
    sol = []
    lines = []
    while (n != 4):
        lines.append(n)
        n = int(input())

    for l in lines:
        sol.append(process(l, 1))

    for s in sol:
        print(s[0], s[1])

if __name__ == "__main__":
    main()