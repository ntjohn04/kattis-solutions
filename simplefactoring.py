from functools import reduce
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def process(a, b, c):
    a_facts = factors(a)
    c_facts = factors(c)

    for d in a_facts:
        f = a / d
        for e in c_facts:
            g = c / e
            if b == e*f + g*d:
                return "YES"
            
    return "NO"

def main():
    n = int(input())

    sols = []
    for i in range(n):
        L = input()
        L = L.split(sep=" ")
        L = [int(x) for x in L]

        sols.append(process(L[0], L[1], L[2]))
    
    for sol in sols:
        print(sol)

if __name__ == "__main__":
    main()