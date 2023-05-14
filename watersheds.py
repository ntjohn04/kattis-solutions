import sys
import copy

sys.setrecursionlimit(999999999)

alph = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'test']

PRINT = False

def findSink(smap, a):
    if PRINT: print("point:", a)
    x = a[0]
    y = a[1]
    if PRINT: print(x, y)
    if PRINT: print("value at point:", smap[x][y])
    if PRINT: print()

    minV = 10001
    direc = "_"
    cord = 0

    #south
    if x < len(smap)-1:
        if PRINT: print("checking south")
        s = smap[x+1][y]
        if PRINT: print(s)
        if min(s, minV) == s and smap[x][y] > s:
            minV = s
            direc = "S"
            cord = (x+1, y)

    #east
    if y < len(smap[0])-1:
        if PRINT: print("checking east")
        e = smap[x][y+1]
        if PRINT: print(e)
        if min(e, minV) == e and smap[x][y] > e:
            minV = e
            direc = "E"
            cord = (x, y+1)

    #west
    if y > 0:
        if PRINT: print("checking west")
        w = smap[x][y-1]
        if PRINT: print(w)
        if min(w, minV) == w and smap[x][y] > w:
            minV = w
            direc = "W"
            cord = (x, y-1)

    #north
    if x > 0:
        if PRINT: print("checking north")
        n = smap[x-1][y]
        if PRINT: print(n)
        if min(n, minV) == n and smap[x][y] > n:
            minV = n
            direc = "N"
            cord = (x-1, y)

    if direc != "_":
        if PRINT: print("going:", direc)
        return findSink(smap, cord)
    else:
        if PRINT: print("sink at:", (x, y))
        return (x, y)

def process(smap, h, w):
    sinkDict = {}
    basinCnt = 0

    rmap = copy.deepcopy(smap)

    if PRINT: print(smap)

    for i in range(h):


        for j in range(w):


            sink = findSink(smap, (i, j))
            if sink not in sinkDict:
                if PRINT: print("new sink found:", sink)
                if PRINT: print()
                if PRINT: print("basinCnt:", basinCnt+1)
                try:
                    sinkDict[sink] = alph[basinCnt]
                except:
                    print("rmap:")
                    print(rmap)
                    print("exitng")
                    sys.exit()
                basinCnt += 1
            rmap[i][j] = sinkDict[sink]

    if PRINT: print(rmap)
    if PRINT: print(smap)
    if PRINT: print("basins:", basinCnt)

    return rmap

def display(sol):
    for i, s in enumerate(sol):
        print("Case #" + str(i+1) + ":")
        for r in s:
            for q in r:
                print(q, end=" ")
            print()

def main():
    global h
    global w

    T = int(input())

    sol = []
    for i in range(T):

        dim = input()
        dim = dim.split(sep=" ")
        if PRINT: print("dimensions:", dim)
        h = int(dim[0])
        w = int(dim[1])
        if PRINT: print("dimensions:", h, w)

        smap = []
        for j in range(h):
            l = input()
            l = l.split(sep=" ")

            for k in range(w):
                l[k] = int(l[k])

            #print(l)
            smap.append(l)

        sol.append(process(smap, h, w))

    display(sol)


if __name__ == "__main__":
    main()