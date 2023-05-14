def main():
    n = int(input())

    i = n + 1
    j = n - 1

    while(i % 100 != 99 and (j % 100 != 99 or j < 0)):
        i += 1
        j -= 1

    if (i % 100 == 99):
        print(i)
    else:
        print(j)

if __name__ == "__main__":
    main()