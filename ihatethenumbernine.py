mod = 1000000007
T = int(input())

for i in range(T):
    b = int(input())
    print((pow(9, b, mod) - pow(9, b-1, mod)) % mod)