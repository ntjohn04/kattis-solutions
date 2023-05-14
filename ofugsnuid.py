def main():
    n = int(input())
    lines = []
    for i in range(n):
        lines.append(int(input()))

    lines.reverse()
    for l in lines:
        print(l)

if __name__ == "__main__":
    main()