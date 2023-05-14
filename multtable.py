from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def process(n, m):
    facts = list(factors(m))
    facts.sort()

    A = len(facts)

    newfacts = [x for x in facts if x <= n]

    B = len(newfacts)

    result = B-(A-B)

    if result < 0:
        print(0)
    else:

        print(result)

def main():
    N = input()
    N = N.split(sep=' ')

    n = int(N[0])
    m = int(N[1])

    process(n, m)

if __name__ == "__main__":
    main()