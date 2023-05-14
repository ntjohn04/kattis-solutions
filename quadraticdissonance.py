def process(l):
    a = l[0]
    b = l[1]
    c = l[2]
    d = l[3]

    if (a == c):
        
        if b > d:
            f_min = -a/2
            print(f_min, f_min**2 + a*f_min + b)
            return
        else:
            g_min = -c/2
            print(g_min, g_min**2 + c*g_min + d)
            return
        

    intersect = (d - b) / (a - c)

    f_min = -a/2
    g_min = -c/2

    if (intersect <= f_min and intersect >= g_min) or (intersect >= f_min and intersect <= g_min):
        print(intersect, intersect**2 + a*intersect + b)

    else:
        mins = [f_min**2 + a*f_min + b, g_min**2 + c*g_min + d]
        index_max = max(range(len(mins)), key=mins.__getitem__)
        if index_max == 0:
            print(f_min, mins[0])
        if index_max == 1:
            print(g_min, mins[1])

def main():
    L = input()
    L = L.split(sep=" ")
    L = [int(x) for x in L]

    process(L)

if __name__ == "__main__":
    main()