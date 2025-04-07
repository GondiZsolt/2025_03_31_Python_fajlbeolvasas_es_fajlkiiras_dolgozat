"""
Olvasd be az f1.txt adatait, majd oldd meg az alábbi feladatokat!


1. Hány versenyző szerepel a fájlban?
2. Melyik versenyző nyerte a legtöbb futamot?
3. Ki teljesített a legtöbb futamot?
4. Átlagosan hány futamot teljesítettek a versenyzők?"

A megoldott feladatokat a kiirt_adatok nevű mappába hozd létre statisztika.txt néven!
"""
nevek = []
with open("beolvasando_adatok/f1.txt", "r", encoding="utf-8") as f:
    next(f)
    adatok = f.read().splitlines()
    

    for sor in adatok:
        print(sor.split(";"))
        Név = sor.split(";")[0]
        nevek.append(Név)
        Csapat = sor.split(";")[1]
        Győzelmek_száma = sor.split(";")[2]
        gyozelem = []
        gyozelem.append(Győzelmek_száma)
        max(gyozelem) = nyertes
        Teljesített_futamok_száma = sor.split(";")[3]
        futamok = 0
        futamok += int(Teljesített_futamok_száma)
        





# print(f"A beolvasott fájlban összesen {len[nevek]} versenyző szerepel.")
print(f"A legtöbb futamot nyert versenyző: {nyertes}")
print(f"A legtöbb futamot teljesített versenyző: {nevek[futamok]}")
print(f"Az átlagos futamszám: ____")