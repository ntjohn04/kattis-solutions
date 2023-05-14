def process(l, m):
    for kn in l:
        if kn not in m:
            return kn

def main():
    n = int(input())

    L = input()
    L = L.split(sep=" ")

    M = input()
    M = M.split(sep=" ")

    print(process(L, M))

if __name__ == "__main__":
    main()