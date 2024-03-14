#1
sez = ['helo', "jabka1", 'seven', "apap"]
cena = [10, 12, 13, 14, 15]
pocet = []
for item in sez:
    pocet.append(len(item))
    print(f'{item} ma delku {len(item)}')
print("cv2",pocet)

#2
dictionary1 = {}

for cenik in range(len(sez)):
    dictionary1[sez[cenik]] = cena[cenik]
    
print("\n","cv2",dictionary1)

#3 dopisat
#text = input("Vloz: ")
#seznam_slov = text.split()
#print(seznam_slov)
#
#for item in seznam_slov:
#    if seznam_slov.get(item):
#    seznam_slov[item] +=1      

#4
cislo = int(input("NApis: "))

i=1
faktorial = 1
if cislo > 0:
    while i<=cislo:
        faktorial = faktorial * i
        i += 1
    else: print("\n","cv2","zkus")
print("\n","cv3",faktorial)