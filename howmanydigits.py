import math

def main():
    while True:
        try:
            print((math.floor(math.lgamma(int(input())+1)/math.log(10))+1))
        except EOFError:
            break

if __name__ == "__main__":
    main()