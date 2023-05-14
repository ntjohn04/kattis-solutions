import re

def get_digit(number, n):
    return number // 10**n % 10

def createNum(num):
    if num > 9:
        ty = get_digit(num, 1)
        ne = get_digit(num, 0)

        s1 = ""
        s2 = ""

        if ty == 1:
            if ne == 0:
                return "ten"
            elif ne == 1:
                return "eleven"
            elif ne == 2:
                return "twelve"
            elif ne == 3:
                return "thirteen"
            elif ne == 4:
                return "fourteen"
            elif ne == 5:
                return "fifteen"
            elif ne == 6:
                return "sixteen"
            elif ne == 7:
                return "seventeen"
            elif ne == 8:
                return "eighteen"
            elif ne == 9:
                return "nineteen"

        elif ty == 2:
            s1 = "twenty"
        elif ty == 3:
            s1 = "thirty"
        elif ty == 4:
            s1 = "forty"
        elif ty == 5:
            s1 = "fifty"
        elif ty == 6:
            s1 = "sixty"
        elif ty == 7:
            s1 = "seventy"
        elif ty == 8:
            s1 = "eighty"
        elif ty == 9:
            s1 = "ninety"

        if ne == 0:
            s2 = ""
        elif ne == 1:
            s2 = "one"
        elif ne == 2:
            s2 = "two"
        elif ne == 3:
            s2 = "three"
        elif ne == 4:
            s2 = "four"
        elif ne == 5:
            s2 = "five"
        elif ne == 6:
            s2 = "six"
        elif ne == 7:
            s2 = "seven"
        elif ne == 8:
            s2 = "eight"
        elif ne == 9:
            s2 = "nine"

        if len(s2) > 1:
            return s1 + "-" + s2
        else:
            return s1

    else:
        ne = get_digit(num, 0)

        if ne == 0:
            return "zero"
        elif ne == 1:
            return "one"
        elif ne == 2:
            return "two"
        elif ne == 3:
            return "three"
        elif ne == 4:
            return "four"
        elif ne == 5:
            return "five"
        elif ne == 6:
            return "six"
        elif ne == 7:
            return "seven"
        elif ne == 8:
            return "eight"
        elif ne == 9:
            return "nine"

def getNumbers(s):
    arr = re.findall(r'[0-9]+', s)
    return arr

def process(l):
    nums = getNumbers(l)
    #print(nums)
    for num in nums:
        b = createNum(int(num))
        #print(b)
        l = l.replace(num, b)
        l = l[0].upper() + l[1:len(l)]

    return l

def main():
    sol = []
    lines = []
    
    while True:
        try:
            lines.append(input())
        except EOFError:
            break

    for l in lines:
        print(process(l))

if __name__ == "__main__":
    main()