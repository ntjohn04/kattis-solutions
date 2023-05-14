def main():
    L = input()
    L = L.split()

    Auniq = int(L[0])
    Buniq = int(L[1])

    Areuse = int(L[2])
    Breuse = int(L[3])

    if Areuse > 0 and Breuse > 0:
        print(Areuse*Breuse + Buniq + Auniq)
    
    elif Areuse > 0:
        print(Areuse*Breuse + Buniq)

    elif Breuse > 0:
        print(Areuse*Breuse + Auniq)

    else:
        print(min(Auniq, Buniq))

if __name__ == "__main__":
    main()