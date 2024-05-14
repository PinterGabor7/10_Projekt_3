class Jatekos:

    def __init__(self, sor: str):
        adatok = sor.strip().split(';')
        self.nev = adatok[0]
        self.nem = adatok[1]
        self.szarmazas = adatok[2]
        self.szuletes = int(adatok[3])
        self.nyert = int(adatok[4])
        self.vesztett = int(adatok[5])