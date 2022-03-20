# ADT Chocolademelk
## data

class Chocolademelk:
    def __init__(self,id,):
        self.id = id  # nog geen id toegekend
        self.prijs = 2  # prijs is bekend
        self.credits = 5
        self.extra = []

### functionaliteit
    def voeg_chocolade_toe (self, type) :

        """
        voeg een chocoladeshot toe aan de chocolademelk
        preconditie : chocoladeshot is een integer uit 0,1,2,3
        postconditie : de prijs van de chocolademelk is verhoogd met 1 EUR
        : param chocoladeshot : een integer die de kleur van de chocoladeshot
         voorstelt :
         0 = WIT
         1 = MELK
         2 = BRUIN
         3 = ZWART
        : return : geeft niets terug
        """
        if (type == 0):
            self.extra.append("wit")
        elif (type == 1):
            self.extra.append("melk")
        elif (type == 2):
            self.extra.append("bruin")
        elif (type == 3):
            self.extra.append("zwart")
        else:
            pass
        self.prijs += 1

    def voeg_honing_toe(self):
        """
        voeg honing toe aan de chocolademelk
        preconditie: geen preconditie
        postconditie: de prijs van de chocolademelk is verhoogd met 0,50 EUR
        :return: geeft niets terug
        """
        self.extra.append("honing")
        self.prijs += 0.50

    def voeg_marshmallow_toe(self):
        """
        voeg marshmallow toe aan de chocolademelk
        preconditie: geen preconditie
        postconditie: de prijs van de chocolademelk is verhoogd met 0,75 EUR
        :return: geeft niets terug
        """

        self.extra.append("marshmallow")
        self.prijs += 0.75

    def voeg_chilipeper_toe(self):
        """
        voeg chilipeper toe aan de chocolademelk
        preconditie: geen preconditie
        postconditie: de prijs van de chocolademelk is verhoogd met 0,25 EUR
        :return: geeft niets terug
        """

        self.extra.append("chilipeper")
        self.prijs += 0.25
