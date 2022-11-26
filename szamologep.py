def szamologep():  # meghívja az adatbekerés metódust, és az ott kapott visszatérési értéket felhasználja
    # lokális változó csak a függvényen belül látszik
    # függvény és metódus UA.
    szam1 = float(adatbekeres("Adj meg egy számot: "))
    muvelet = adatbekeres("műveleti jel:")
    szam2 = float(adatbekeres("Adj meg egy számot: "))
    szoveg = ""
    er = 0

    if muvelet == "*":
        er = szoroz(szam1, szam2)
    elif muvelet == "/":
        er = oszt(szam1, szam2)
    elif muvelet == "+":
        er = osszead(szam1, szam2)
    elif muvelet == "-":
        er = kivon(szam1, szam2)
    else:
        szoveg += "nem értelmehető a művelet"

    kiiras(szam1, muvelet, szam2, er, szoveg)   # paraméter átadása ebből a fv-ből, a kiiras fv-be


def osszead(a, b):
    return a + b


def kivon(a, b):
    return a - b


def szoroz(a, b):
    return a * b


def oszt(a, b):
    return a / b


def adatbekeres(szoveg):

    print("-" * 20)
    kismacska = input(szoveg)
    return kismacska  # visszatérési érték


def kiiras(szam1, muvelet, szam2, er, szoveg):
    print("-" * 20)
    if szoveg == "":
        print(f"{szam1}{muvelet}{szam2} = {er}")

    else:
        print(szoveg)
