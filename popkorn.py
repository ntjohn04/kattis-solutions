def process(n):
    a = n/4
    return 4*a*(a-1)/2 + 4

def main():
    n = int(input())

    bags = process(n)
    print(int(bags))

if __name__ == "__main__":
    main()