def get_max(mat, i, j):
    col = j + i

    maxv = -10e9
    for p in range(0, i+1):
        if mat[p][col] == None:
            continue

        if mat[p][col] >= maxv:
            maxv = mat[p][col]

    return maxv

def final_max(arr):
    max = -10e9
    for num in arr:
        if num == None:
            continue

        if num > max:
            max = num

    return max

def new_maxes(a, b):
    if b == None or a > b:
        return a
    
    return b

def update_maxes(colmaxes, j, mat, n):
    for i in range(len(colmaxes)):
        if i > j:
            colmaxes[i] = new_maxes(colmaxes[i], mat[i-j][i])

def retrieve_maxes(colmaxes, i):
    return colmaxes[i]

def process(l, n):
    a = n-1
    last = l[a]

    mat = [[None for x in range(n)] for y in range(n)]

    mat[0][a] = last
    mat[1][a] = last
    for i in range(1, n):
        mat[i][a-i] = l[a-i] + last

    colmaxes = [-10e9]*n

    for j in range(a, a//2, -1):
        update_maxes(colmaxes, j, mat, a)
        for i in range(1, a-j):
            mat[i][j] = l[j] + retrieve_maxes(colmaxes, j+i)

    for j in range(a//2, 0, -1):
        update_maxes(colmaxes, j, mat, a)
        for i in range(1, j+1):
            mat[i][j] = l[j] + retrieve_maxes(colmaxes, j+i)
    
    for j in range(a):
        mat[j][0] = l[0] + get_max(mat, j, 0)

    print(int(final_max([row[0] for row in mat])))

def main():
    n = int(input())
    L = input()
    L = L.split(sep=" ")
    L = [int(x) for x in L]
        
    process(L, n)

if __name__ == "__main__":
    main()