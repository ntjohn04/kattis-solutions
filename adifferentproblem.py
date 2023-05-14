def process(L):
    L = L.split(sep=" ")

    return abs(int(L[0]) - int(L[1]))

def main():
    lines = []
    
    while True:
        try:
            lines.append(input())
        except EOFError:
            break

    for s in lines:
        print(process(s))

if __name__ == "__main__":
    main()