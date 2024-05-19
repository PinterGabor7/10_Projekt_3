from asztalitenisz import Jatekos

jatekosok: list[Jatekos] = []

def main():
    beolvasas() 
    print(f'3. feladat: A fájlban {len(jatekosok)} játékos adata szerepel.')
    noi_jatekosok()
    legtobb_ny()
    legfiatalabb()
    vesztes()
    jatekosok_szama()
    uj_stat()

def noi_jatekosok():
    print('\n4. feladat: A női játékosok:')
    for j in jatekosok: 
        if j.nem == 'Nő':       
            print(f'\t{j.nev}')

def legtobb_ny():
    print('\n5. feladat: Legtöbb mérkőzést nyert játékos: ')
    legtobb_ny = jatekosok[0]
    for j in jatekosok:
        if j.nyert > legtobb_ny.nyert:
            legtobb_ny = j
    print(f'\t{legtobb_ny.nev} {legtobb_ny.nyert}')

def legfiatalabb():
    legfiatalabb = jatekosok[0]
    for j in jatekosok:
        if legfiatalabb.szuletes < j.szuletes:
            legfiatalabb = j
    print(f'\n6. feladat: A legfiatalabb játékos {legfiatalabb.nev}, {2024 - legfiatalabb.szuletes} éves')

def vesztes():
    tveszt = int(input('\n7. feladat: Írjon be egy számot: '))
    print(f'{tveszt}-nél/nál több mérkőzést vesztett játékosok:')
    for j in jatekosok:
        if tveszt < j.vesztett:
            print(f'\t{j.nev}')
    if tveszt > j.vesztett:
        print('\tNem található ilyen játékos')  
            

def jatekosok_szama():
    print('\n8. feladat: Játékosok száma más országokban')
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
    jatekos = input('\n9. feladat: Kérem a keresett játékos nevét: ')
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
