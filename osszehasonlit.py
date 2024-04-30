print('Téglalap területek összehasonlítása')
a1 = int(input('1. téglalap a oldal hossza: '))
b1 = int(input('1. téglalap b oldal hossza: '))
terulet1 = a1 * b1
a2 = int(input('2. téglalap a oldal hossza: '))
b2 = int(input('2. téglalap b oldal hossza: '))
terulet2 = a2 * b2
if terulet1 > terulet2:
    print("Az első téglalap területe nagyobb.")
elif terulet1 < terulet2:
    print('A második téglalap területe nagyobb.')
else:
    print('A téglalapok területe egyenlő')