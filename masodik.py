def main():
    belepesek = dict()
    belepesek['otto123'] = 1
    belepesek['peti__'] = 8
    belepesek['XferiX'] = 7
    belepesek['_bela_'] = 5
    jelszavak = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    felhnev = input('Adja meg a felhasználónevét: ')
    jelszo = input('Adja meg a jelszavát (1-9 közé eső szám): ')
    while jelszo not in jelszavak:
        jelszo = input('Adja meg a jelszavát (1-9 közé eső szám): ')
    jelszo = int(jelszo)
    if felhnev not in belepesek.keys() or jelszo != belepesek[felhnev]:
        print('Nem megfelelő felhasználónév vagy jelszó.')
    else:
        print('Belépés engedélyezve.')

main()