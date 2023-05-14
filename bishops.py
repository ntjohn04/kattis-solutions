l = []
while True:
    try:
        l.append(int(input()))
    except EOFError:
        break
for s in l:
    print(2*s - 2) if s > 1 else print(1)