import re

def main():
    n = int(input())

    l = input()

    if n > 9:
        ls1 = l[0:9]
        ls2 = l[9:len(l)]

        if ls1 == "123456789":

            hundred = False
            if "100" in ls2:
                ls2 = ls2[:-3]
                hundred = True

            arr = re.findall('..', ls2)
            if hundred:
                arr.append("100")

            for i in range(10, n+1):
                if str(i) not in arr:
                    print(i)
                    return

        else:
            for i in range(1, 10):
                if str(i) not in ls1 or (i == 1 and ls1.index("1") != 0):
                    print(i)
                    return

    else:
        for i in range(1, n+1):
            if str(i) not in l or (i == 1 and l.index("1") != 0):
                print(i)
                return

if __name__ == "__main__":
    main()