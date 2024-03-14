# knihovna nakupu a kategorie drah0
potraviny = ['smetana', "jabka", 'seven', "ananas"]
cena = [10, 22, 33, 44, 15]
kategorie = ["levne", "stredne drahe", "drahe"]
katalog = {}
for polozka in range(len(potraviny)):
    if cena[polozka] < 15:
        katalog[potraviny[polozka]] = [cena[polozka], kategorie[0]]
    elif cena[polozka] >= 15 and cena[polozka] < 23:
        katalog[potraviny[polozka]] = [cena[polozka], kategorie[1]]
    else: katalog[potraviny[polozka]] = [cena[polozka], kategorie[2]]
print(katalog)