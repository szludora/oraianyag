"""def betukszama():
    szoveg = "elke"
    betuk = []
    db = 0
    i = 0
    betu = szoveg[i]

    while i < len(szoveg):
        x = 0

        if szoveg[i] not in betuk:
            betuk.append(betu)

        while x < len(szoveg):
            if szoveg[x] == betu[i]:
                db += 1
            x += 1
        i += 1
    print(szoveg, betuk, db)"""



szam = 2

def fv1():
    szam1 = 3
    global szam     # ha megváltoztatod a globális értékét, meg kell hívni, amúgy nem

    print(f"\nfv1 szám1 lokális: {szam1}")
    # print(f"fv1: {szam2}")
    print(f"fv1 globális:  {szam}")

    szam = 12
    print(f"fv1 változtatott globális szam: {szam}")
    # return szam1
    fv3(szam1)  # oátadom az értéket a fv3-nak

def fv2():
    szam2 = 4

    print(f"\nfv2 globális {szam}")
    # print(f"fv2: {szam1}")
    print(f"fv2 lokális {szam2}")
    # szam1 = fv1()
    return szam

def fv3(szam1):
    global szam
    print(f"\nfv3 globális: {szam}")
    print(f"szám1 kapott: {szam1}")  # megkapta a szam1-et de módosítani nem tudja
    print(f"szám1 módosított: {szam1 - 2}")
