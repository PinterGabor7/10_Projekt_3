class Jatekos:

    def __init__(self, sor: str):
        adatok = sor.strip().split()
        self.nev = adatok[0]
        self.szuletes = int(adatok[1])
        self.nyert = int(adatok[2])
        self.vesztett = int(adatok[3])