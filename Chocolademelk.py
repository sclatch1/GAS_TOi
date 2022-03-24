# thomassen maakt, David test
# ADT Chocolademelk
## data
from arraybased_stack import MyStack
#from circulairedubbelgelinkte_ketting import LinkedChain
from Chocoladeshot import Chocoladeshot
from Honing import Honing
from Marshmallow import Marshmallow
from Chilipeper import Chilipeper


input = MyStack(100)
shot = Chocoladeshot()
honing = Honing()
marshmellow = Marshmallow()
chilipeper = Chilipeper()

class Chocolademelk:
    def __init__(self,id,):
        self.id = id  # nog geen id toegekend
        self.prijs = 2  # prijs is bekend
        self.credits = 5


### functionaliteit
    def voeg_chocolade_toe (self) :

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

        if(id == 0):
            input.push(shot.wit)
            self.prijs += 1
        if(id == 1):
            input.push(shot.melk)
            self.prijs += 1
        if(id == 2):
            input.push(shot.bruin)
            self.prijs += 1
        if(id == 3):
            input.push(shot.zwart)
            self.prijs += 1


        pass

    def voeg_honing_toe(self):
        """
        voeg honing toe aan de chocolademelk
        preconditie: geen preconditie
        postconditie: de prijs van de chocolademelk is verhoogd met 0,50 EUR
        :return: geeft niets terug

        """
        input.push(honing)
        self.prijs += 0.5
        pass

    def voeg_marshmallow_toe(self):
        """
        voeg marshmallow toe aan de chocolademelk
        preconditie: geen preconditie
        postconditie: de prijs van de chocolademelk is verhoogd met 0,75 EUR
        :return: geeft niets terug
        """
        input.push(marshmellow)
        self.prijs += 0.75
        pass
    def voeg_chilipeper_toe(self):
        """
        voeg chilipeper toe aan de chocolademelk
        preconditie: geen preconditie
        postconditie: de prijs van de chocolademelk is verhoogd met 0,25 EUR
        :return: geeft niets terug
        """
        input.push(chilipeper)
        self.prijs += 0.25
        pass