def process(arr):
    spacings = set()
    a = 0
    for i in range(1, len(arr)):
        if arr[i] == "*":
            spacings.add(i-a)
            a = i

    if len(spacings) <= 1:
        return "EVEN"
    return "NOT EVEN"

def main():
    n = input()
    spacings = []
    while (n != "END"):
        arr = [x for x in n]
        spacings.append(process(arr))
        n = input()

    for i, space in enumerate(spacings):
        print(str(i+1) + " " + space)


if __name__ == "__main__":
    main()