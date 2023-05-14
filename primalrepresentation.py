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

def process(n):
    facts = list(prime_factors(abs(n)))

    cnts = {}
    for fact in facts:
        cnts[fact] = facts.count(fact)

    strn = ""
    for key, item in cnts.items():
        if item > 1:
            strn += str(key) + "^" + str(item) + " "
        else:
            strn += str(key) + " "

    if n < 0:
        strn = "-1 " + strn

    print(strn)

def main():
    lines = []
    while True:
        try:
            lines.append(int(input()))
        except EOFError:
            break

    for l in lines:
        process(l)

if __name__ == "__main__":
    main()