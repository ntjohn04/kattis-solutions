def process(L):
    if "PROBLEM" in L.upper():
        return "yes"
    else:
        return "no"

def main():
    sol = []
    lines = []
    
    while True:
        try:
            lines.append(input())
        except EOFError:
            #lines_str = '\n'.join(lines)
            #print(lines_str)

            break

    for s in lines:
        print(process(s))

if __name__ == "__main__":
    main()