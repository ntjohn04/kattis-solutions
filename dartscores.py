def process(n):

    if n < 3:
        if n == 2:
            return [1, 1], [1, 1]
        else:
            return [1], [1]


    for a in range(1, 4):
        for b in range(1, 4):
            for c in range(1, 4):


                for i in range(1, 21):
                    for j in range(1, 21):
                        for k in range(1, 21):
                            
                            #print(a, i, b, j, c, k)

                            if a*i + b*j + c*k == n:
                                coefs = [a, b, c]
                                nums = [i, j, k]
                                return coefs, nums
                
    return "impossible", []

def main():
    n = int(input())

    coefs, nums = process(n)

    if coefs == "impossible":
        print("impossible")
        return

    for i, c in enumerate(coefs):
        if c == 1:
            coefs[i] = "single"
        elif c == 2:
            coefs[i] = "double"
        elif c == 3:
            coefs[i] = "triple"

    for i in range(len(coefs)):
        print(coefs[i], nums[i])

if __name__ == "__main__":
    main()