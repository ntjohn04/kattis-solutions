from sys import exit
import random

def make_choice(magnum):
    if magnum == 97:
        return 2
    if magnum == 98:
        return 1

    if (magnum + 1) % 3 == 0:
        return 1
    if (magnum + 2) % 3 == 0:
        return 2

    return random.randrange(1, 3)


def main():
    magnum = 0
    while (magnum != 99):
        choice = make_choice(magnum)
        magnum += choice
        print(magnum)
        if magnum == 99:
            exit(0)

        PCchoice = int(input())
        magnum = PCchoice

    exit(0)
    

if __name__ == "__main__":
    main()