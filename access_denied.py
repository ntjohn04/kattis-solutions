arr = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890"
sol = []
tot = 0

def findLength():
    for i in range(20):
        pwd = "A"
        for j in range(i):
            pwd = pwd + "A"

        print(pwd)
        resp = input()
        if resp == "ACCESS GRANTED":
            return 200, -1
        
        t = [int(s) for s in resp.replace("(", "").split() if s.isdigit()][0]
        
        if t != 5:
            return i, t

def crack(l, t, i):
    global tot

    b = t
    c = 0
    while b == t:

        pwd = ""
        for h in sol:
            pwd = pwd + h

        pwd = pwd + arr[c]

        while len(pwd) != l + 1:
            pwd = pwd + "A"

        print(pwd)
        tot += 1
        resp = input()

        if resp == "ACCESS GRANTED":
            return -1

        b = [int(s) for s in resp.replace("(", "").split() if s.isdigit()][0]

        if c == 0:
            pwd = ""
            for h in sol:
                pwd = pwd + h

            pwd = pwd + arr[c+1]

            while len(pwd) != l + 1:
                pwd = pwd + "A"

            print(pwd)
            tot += 1
            resp = input()

            if resp == "ACCESS GRANTED":
                return -1

            u = [int(s) for s in resp.replace("(", "").split() if s.isdigit()][0]

            if u < b:
                sol.append(arr[c])
                return b


        c += 1

    sol.append(arr[c-1])

    return b

def main():

    l, t = findLength()

    if l == 200:
        return

    for i in range(20):
        t = crack(l, t, i)
        if t == -1 or tot == 2500:
            break

if __name__ == "__main__":
    main()