def main():
    L = input()
    L = [*L]

    #print(L)

    stri = ['P', 'E', 'R']*(len(L) // 3)

    #print(stri)

    days = 0
    for i in range(len(L)):
        if L[i] != stri[i]:
            days += 1

    print(days)

if __name__ == "__main__":
    main()
