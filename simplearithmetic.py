from decimal import *

def main():
    getcontext().prec = 30
    l = input()
    l = l.split(sep=" ")
    l = [Decimal(x) for x in l]

    a = l[0]
    b = l[1]
    c = l[2]

    r = a*b/c

    if "." not in str(r):
        print(str(r) + ".00000000")
    else:
        print(r)

if __name__ == "__main__":
    main()