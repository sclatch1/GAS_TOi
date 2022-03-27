# ADT Chocoladeshot
## data

class Chocoladeshot:
    def __init__(self, soort, vervaldatum):
        #soorten chocolade
        if (soort == 0):
            self.soort = "wit"
        if (soort == 1):
            self.soort = "bruin"
        if (soort == 2):
            self.soort = "zwart"
        if (soort == 3):
            self.soort = "melk"

        self.prijs = 1 # prijs is bekend
        self.vervaldatum = vervaldatum # vervaldatum is onbekend
        self.credit = 1

### functionaliteit
