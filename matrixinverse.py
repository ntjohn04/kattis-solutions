import copy

def process(l1, l2):
    a = [[eval(i) for i in l1.split()], [eval(i) for i in l2.split()]]

    b = copy.deepcopy(a)

    d = a[0][0]*a[1][1] - a[0][1]*a[1][0]

    b[0][0] = a[1][1] // d
    b[1][1] = a[0][0] // d

    b[0][1] = -a[0][1] // d
    b[1][0] = -a[1][0] // d

    return b

def display(sol):
    for i, s in enumerate(sol):
        print("Case " + str(i+1) + ":")
        print(s[0][0], s[0][1])
        print(s[1][0], s[1][1])

def main():
    sol = []
    lines = []
    
    while True:
        try:
            lines.append(input())
        except EOFError:
            break

    for i in range(len(lines) // 3):
        sol.append(process(lines[3*i], lines[3*i+1]))

    display(sol)

if __name__ == "__main__":
    main()