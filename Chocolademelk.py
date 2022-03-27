# thomassen maakt, David test
# ADT Chocolademelk
## data
from arraybased_stack import MyStack
from Chocoladeshot import Chocoladeshot
from Honing import Honing
from Marshmallow import Marshmallow
from Chilipeper import Chilipeper


class Chocolademelk:
    def __init__(self):
        self.prijs = 2  # prijs is bekend
        self.credits = 5
        self.ingredienten = [0, 0, 0, 0, 0, 0, 0]

    ### functionaliteit
    def voeg_chocolade_toe(self, soort):

        """
        voeg een chocoladeshot toe aan de chocolademelk
        preconditie : chocoladeshot is een integer uit 0,1,2,3
        postconditie : de prijs van de chocolademelk is verhoogd met 1 EUR
        : param chocoladeshot : een integer die de kleur van de chocoladeshot
         voorstelt :
         0 = WIT
         1 = BRUIN
         2 = ZWART
         3 = MELK
        : return : geeft niets terug
        """

        if (soort == 0):
            self.ingredienten[3] += 1
            self.prijs += 1
        if (soort == 1):
            self.ingredienten[4] += 1
            self.prijs += 1
        if (soort == 2):
            self.ingredienten[5] += 1
            self.prijs += 1
        if (soort == 3):
            self.ingredienten[6] += 1
            self.prijs += 1

        pass

    def voeg_honing_toe(self):
        """
        voeg honing toe aan de chocolademelk
        preconditie: geen preconditie
        postconditie: de prijs van de chocolademelk is verhoogd met 0,50 EUR
        :return: geeft niets terug

        """
        self.ingredienten[0] += 1
        self.prijs += 0.5
        pass

    def voeg_marshmallow_toe(self):
        """
        voeg marshmallow toe aan de chocolademelk
        preconditie: geen preconditie
        postconditie: de prijs van de chocolademelk is verhoogd met 0,75 EUR
        :return: geeft niets terug
        """
        self.ingredienten[1] += 1
        self.prijs += 0.75
        pass

    def voeg_chilipeper_toe(self):
        """
        voeg chilipeper toe aan de chocolademelk
        preconditie: geen preconditie
        postconditie: de prijs van de chocolademelk is verhoogd met 0,25 EUR
        :return: geeft niets terug
        """
        self.ingredienten[2] += 1
        self.prijs += 0.25
        pass
