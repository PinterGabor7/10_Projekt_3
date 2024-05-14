from asztalitenisz import Jatekos

jatekosok: list[Jatekos] = []

def main():
    beolvasas() 
    print(f'2. feladat: A fájlban {len(jatekosok)} játékos adata szerepel.')
    jatekos_kereses()
    jatekosok_szama()

def jatekos_kereses():
    jatekos = input('\nKérem a keresett játékos nevét: ')
    i = 0
    while i < len(jatekosok) and jatekos != jatekosok[i].nev:
        i += 1
    if i < len(jatekosok):
        print(f'\t{jatekosok[i].nev} {jatekosok[i].nyert} versenyt nyert.')
    else: 
        print('\tNincs ilyen versenyző!')

def jatekosok_szama():
    orszagok = {}
    for j in jatekosok:
        orszag = j.szarmazas
        if orszag in orszagok:
            orszagok[orszag] += 1
        else:
            orszagok[orszag] = 1
    for orszag, jatekosok_szama in orszagok.items():
        print(f'\t{orszag}: {jatekosok_szama} fő')

def beolvasas():
    f = open('jatekosok.txt', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        jatekosok.append(Jatekos(sor))
    f.close()

main()
