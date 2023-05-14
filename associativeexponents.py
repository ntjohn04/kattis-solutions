import math
from math import log

def main():
    L = input()
    L = L.split(sep=" ")
    L = [int(x) for x in L]

    a = L[0]
    b = L[1]
    c = L[2]

    if a == 1 or c == 1:
        print("What an excellent example!")
        return

    try:
        if math.e >= b:
            raise Exception("dumb")

        if (c*log(b)+log(log(a)) == log(c*b*log(a))):
            print("What an excellent example!")
        else:
            print("Oh look, a squirrel!")
            
    except:
        try:
            x = b ** c * log(a)
            y = c * b * log(a)

            if math.e >= x or math.e >= y:
                raise Exception("stupid")
            
            if (log(x) == log(y)):
                print("What an excellent example!")
                return
            else:
                print("Oh look, a squirrel!")
                return
            
        except:
            if (a ** (b ** c) == (a ** b) ** c):
                print("What an excellent example!")
                return
            else:
                print("Oh look, a squirrel!")
                return


if __name__ == "__main__":
    main()