def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)

def main():
    n = int(input())

    for i in range(n):
        print(factorial(int(input())) % 10)

if __name__ == "__main__":
    main()