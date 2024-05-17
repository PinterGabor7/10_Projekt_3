from asztalitenisz import Jatekos

jatekosok: list[Jatekos] = []

def main():
    beolvasas() 
    print(f'2. feladat: A fájlban {len(jatekosok)} játékos adata szerepel.')
    noi_jatekosok()
    jatekos_kereses()
    jatekosok_szama()
    nyeres()
    uj_stat()

def noi_jatekosok():
    print('\nA női játékosok:')
    for j in jatekosok: 
        if j.nem == 'Nő':
            print(f'\t{j.nev}')

def jatekos_kereses():
    jatekos = input('\nKérem a keresett játékos nevét: ')
    i = 0
    while i < len(jatekosok) and jatekos != jatekosok[i].nev:
        i += 1
    if i < len(jatekosok):
        print(f'\t{jatekosok[i].nev} {jatekosok[i].nyert} versenyt nyert.')
    else: 
        print('\tNincs ilyen versenyző!')

def nyeres():
    tnyeres = int(input('\nÍrjon be egy számot: '))
    print(f'{tnyeres}-nél/nál több mérkőzést nyert játékosok:')
    for j in jatekosok:
        if tnyeres < j.nyert:
            print(f'\t{j.nev}')

def jatekosok_szama():
    print('\nJátékosok száma más országokban')
    orszagok = {}
    for j in jatekosok:
        orszag = j.szarmazas
        if orszag in orszagok:
            orszagok[orszag] += 1
        else:
            orszagok[orszag] = 1
    for orszag, jatekosok_szama in orszagok.items():
        print(f'\t{orszag}: {jatekosok_szama} fő')
      
def uj_stat():
    jatekos = input('\nKérem a keresett játékos nevét: ')
    i = 0
    while i < len(jatekosok) and jatekos != jatekosok[i].nev:
        i += 1
    if i < len(jatekosok):
        print(f'\t{jatekosok[i].nev} {jatekosok[i].nyert} versenyt nyert és {jatekosok[i].vesztett} versenyt vesztett.')
    else: 
        print('\tNincs ilyen versenyző!')
    nyert = int(input(f'{jatekosok[i].nev} új nyert mérkőzéseinek száma: '))
    vesztett = int(input(f'{jatekosok[i].nev} új vesztett mérkőzéseinek a száma: '))
    for j in jatekosok:
        j.nyert += nyert
        j.vesztett += vesztett

    f = open('jatekosok.txt', 'w', encoding='utf-8')
    f.write('Név; Nem; Származás; Születési év; Nyert mérkőzések; Vesztett mérkőzések\n')
    for j in jatekosok:
        f.write(f'{j.nev};{j.nem};{j.szarmazas};{j.szuletes};{j.nyert};{j.vesztett}\n')

    f.close()

def beolvasas():
    f = open('jatekosok.txt', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        jatekosok.append(Jatekos(sor))
    f.close()

main()
