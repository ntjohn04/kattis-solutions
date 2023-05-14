def avg(l):
    return sum(l)/len(l)

def process(n, p, l):
    aveg = avg(l)
    i = 0
    while (aveg < p):
        i += 1
        l.append(100)
        aveg = avg(l)
    return i

def main():
    l = input()
    l = l.split(sep=" ")
    l = [int(x) for x in l]

    n = l[0]
    p = l[1]

    if (p == 100):
        print("impossible")
        return

    l = input()
    l = l.split(sep=" ")
    l = [int(x) for x in l]

    print(process(n, p, l))

if __name__ == "__main__":
    main()