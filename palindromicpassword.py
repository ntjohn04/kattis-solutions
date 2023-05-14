def palindrome(n):
    s = str(n)
    if s[0] == s[5] and s[1] == s[4] and s[2] == s[3]:
        return True
    return False

def process(n):
    if palindrome(n):
        return n
    i = 1
    while(True):
        if ((n-i > 100000) and (palindrome(n-i))):
            return n-i
        if palindrome(n+i):
            return n+i
        i += 1

def main():
    n = int(input())

    nums = []
    for i in range(n):
        nums.append(process(int(input())))

    for s in nums:
        print(s)

if __name__ == "__main__":
    main()