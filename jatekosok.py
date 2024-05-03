from asztalitenisz import Jatekos

jatekosok: list[Jatekos] = []

def main():
    beolvasas() 
    print(f'2. feladat: A fájlban {len(jatekosok)} adata szerepel.')

def beolvasas():
    f = open('jatekosok.txt', 'r', encoding='utf-8')
    f.readline()
    for sor in f:
        jatekosok.append(Jatekos(sor))
    f.close()


main()
