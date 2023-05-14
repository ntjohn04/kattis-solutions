def getmod(nums, k):
    if len(nums) == 1:
        return nums[0] % k
    
    return ((nums[0] % k) * (getmod(nums[1:], k))) % k

def getmoditer(nums, k):
    res = 1
    for i in range(len(nums)-1, -1, -1):
        res *= (nums[i]%k)
        res %= k
    return res

def process(nums, k):
    modr = getmoditer(nums, k)
    return modr

def main():
    l = input()
    l = l.split(sep=" ")

    n = int(l[0])
    k = int(l[1])

    nums = []
    for i in range(n):
        nums.append(int(input()))

    r = process(nums, 2**k)

    if r == 0:
        print(1)
    else:
        print(0)

if __name__ == "__main__":
    main()