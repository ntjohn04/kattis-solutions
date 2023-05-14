def process(n, m):
    zeroes = m.count("0")

    A = len(n)
    if (A-zeroes < 0):
        result = ["0", "."]

        for i in range(A-zeroes, 0, 1):
            result.append("0")
        for dig in n:
            result.append(dig)

        B = len(result)
        i = B-1
        while (result[i] == "0"):
            result.pop(i)
            i -= 1

        for i, r in enumerate(result):
            if (r != B-1):
                print(r, end="")
            else:
                print(r)

    else:
        result = n[:A-zeroes] + "." + n[A-zeroes:A]
        result = [x for x in result]

        i = A
        while (result[i] == "0"):
            result.pop(i)
            i -= 1
            
        if result[i] == ".":
            result.pop(i)

        if result[0] == ".":
            result = ["0"] + result

        for i, r in enumerate(result):
            if i != A+1:
                print(r, end="")
            else:
                print(r)

def main():
    n = input()
    m = input()

    process(n, m)

if __name__ == "__main__":
    main()