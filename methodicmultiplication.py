def main():
    a = input()
    b = input()

    aS = a.count("S")
    bS = b.count("S")

    p = aS * bS

    for i in range(p):
        print("S(", end="")

    print("0", end="")

    for i in range(p):
        print(")", end="")

if __name__ == "__main__":
    main()