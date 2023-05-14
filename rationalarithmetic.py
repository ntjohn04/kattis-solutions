from math import gcd

def getLCM(a, b):
    return a * b // gcd(a, b)

def operate(f1, f2, op):
    if op == "*":
        result = [f1[0]*f2[0], f1[1]*f2[1]]
        return result
    
    if op == "/":
        result = [f1[0]*f2[1], f1[1]*f2[0]]
        return result
    
    if op == "+":
        den = getLCM(f1[1], f2[1])

        a = f1[0]*den//f1[1]
        b = f2[0]*den//f2[1]

        result = [a+b, den]
        return result
    
    if op == "-":
        den = getLCM(f1[1], f2[1])

        a = f1[0]*den//f1[1]
        b = f2[0]*den//f2[1]

        result = [a-b, den]
        return result
    
def reduce(f):
    gcdv = gcd(f[0], f[1])
    result = [f[0]//gcdv, f[1]//gcdv]

    if result[1] < 0:
        result = [-x for x in result]

    return result

def process(l):
    frac1 = [int(l[0]), int(l[1])]
    frac2 = [int(l[3]), int(l[4])]
    op = l[2]

    result = operate(frac1, frac2, op)
    result = reduce(result)
    return result

def main():
    n = int(input())

    sol = []
    for i in range(n):
        l = input()
        l = l.split(sep=" ")
        sol.append(process(l))

    for s in sol:
        print(str(s[0]) + " / " + str(s[1]))

if __name__ == "__main__":
    main()
