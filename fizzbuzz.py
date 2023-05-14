def fizzBuzz(x, y, n):
    for i in range(1, n+1):

        a = i % x
        b = i % y

        if a == 0 and b == 0:
            print("FizzBuzz")

        elif a == 0:
            print("Fizz")

        elif b == 0:
            print("Buzz")
        
        else:
            print(i)

def main():
    L = input()
    L = L.split(sep=" ")

    x = int(L[0])
    y = int(L[1])
    n = int(L[2])

    fizzBuzz(x, y, n)

if __name__ == "__main__":
    main()