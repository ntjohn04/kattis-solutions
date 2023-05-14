import math
from functools import reduce
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def is_square(i: int) -> bool:
    return i == math.isqrt(i) ** 2

def process(a, b):
    a_facts = factors(a)
    b_facts = factors(b)

    A = len(a_facts)
    B = len(b_facts)

    if (A == 2 and B == 2 and a != b):
        return "full credit"

    factcombs = set([a*b for a in a_facts for b in b_facts])
    for fact in factcombs:
        if fact != 1 and is_square(fact):
            return "no credit"

    return "partial credit"

def main():
    l = input()
    l = l.split(sep=" ")
    
    a = int(l[0])
    b = int(l[1])

    print(process(a, b))

if __name__ == "__main__":
    main()