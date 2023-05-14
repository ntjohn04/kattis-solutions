from functools import reduce

def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n//i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

def main():
    n = int(input())

    friends = factors(n)
    friends = list(friends)
    friends.sort()

    for i, num in enumerate(friends):
        if i != len(friends)-1:
            print(num-1, end=' ')
        else:
            print(num-1)

if __name__ == "__main__":
    main()