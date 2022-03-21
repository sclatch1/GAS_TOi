# thomas g en david maakt, daan test
# ADT Stocks
## data
import Chilipeper
import Chocolademelk
import Chocoladeshot


class Stocks:
    def __init__(self):
        self.chocolademelk = 0 #aantal niet gekend
        self.wit_chocolade_shot = 0  # aantal niet gekend
        self.bruin_chocolade_shot = 0  # aantal niet gekend
        self.zwart_chocolade_shot = 0  # aantal niet gekend
        self.honing = 0 #aantal niet gekend
        self.marshmallows = 0 #aantal niet gekend
        self.chilipeper = 0 #aantal niet gekend
        self.stock = [self.honing,self.chilipeper,self.bruin_chocolade_shot,self.zwart_chocolade_shot,self.chocolademelk,self.wit_chocolade_shot,self.marshmallows]

### functionaliteit

    def verlaag_stock(self,product,aantal):
        """
            verlaag stock aan met chocolademelk, wit chocolade shot, bruin chocolade shot, zwart chocolade shot, honing, marshmallow, chilipeper
            preconditie: een integer 0,1,2,3,4,5,6
            postconditie: stock wordt verlaag met aantal van elk product
            :param
            aantal: aantal te verlagen producten
            product: een integer 0,1,2,3 die elk een product voorstelt:
            0 = chocolademelk
            1 = honing
            2 = marshmallow
            3 = chilipeper
            4 = wit chocolade shot
            5 = bruin chocolade shot
            6 = zwart chocolade shot
            :return: geeft niks terug
            """
        if product == 0:
            self.chocolademelk -= aantal
        elif product == 1:
            self.honing -= aantal
        elif product == 2:
            self.marshmallows -= aantal
        elif product == 3:
            self.chilipeper = self.chilipeper - aantal
        elif product == 4:
            self.wit_chocolade_shot -= aantal
        elif product == 5:
            self.bruin_chocolade_shot -= aantal
        elif product == 6:
            self.zwart_chocolade_shot -= aantal
        #if self.honing < 0 or self.zwart_chocolade_shot < 0 or self.bruin_chocolade_shot < 0 or self.wit_chocolade_shot < 0 or self.chocolademelk < 0 or self.chilipeper < 0 or self.marshmallows < 0:
        #for ingredient in self.stock:
        #    if ingredient < 0:
        #        ingredient = 0
        else:
            print("inkopen")

    def vul_stock_aan(self,product, aantal):
        """
        vul stock aan met chocolademelk, wit chocolade shot, bruin chocolade shot, zwart chocolade shot, honing, marshmallow, chilipeper
        preconditie: een integer 0,1,2,3,4,5,6 voor product en een integer voor aantal
        postconditie: stock wordt verhoogt met aantal van elk product en kassa wordt verlaagt.
        :param
        aantal: aantal te vullen producten
        product: een integer 0,1,2,3 die elk een product voorstelt:
        0 = chocolademelk
        1 = honing
        2 = marshmallow
        3 = chilipeper
        4 = wit chocolade shot
        5 = bruin chocolade shot
        6 = zwart chocolade shot
        :return: geeft niks terug
        """
        if product == 0:
            self.chocolademelk = aantal
        elif product == 1:
            self.honing = aantal
        elif product == 2:
            self.marshmallows = aantal
        elif product == 3:
            self.chilipeper = aantal
        elif product == 4:
            self.wit_chocolade_shot = aantal
        elif product == 5:
            self.bruin_chocolade_shot = aantal
        elif product == 6:
            self.zwart_chocolade_shot = aantal
        else:
            print("is geen geldige input")

    def controle_verval_datum(self,product,timestamp):
        """
        controleert of vervaldatum van een product voor timestamp komt .
        preconditie: product is een integer, timestamp een een string in de vorm van 00-00-0000
        postcoditie: stock wordt verlaagt
        :param
        timestamp: huidige datum
        product: een integer 0,1,2 die elk een product voorstelt:

        1 = honing
        2 = marshmallow
        3 = chilipeper

        :return: geeft niks terug
        """
        pass
    def print(self):
        output = " chocolademelk " + str(self.chocolademelk) + " honing " + str(self.honing)
        return output

s1 = Stocks()
s1.vul_stock_aan(3,8)
s1.vul_stock_aan(5,8)
s1.vul_stock_aan(9,8)
s1.vul_stock_aan(0,8)

s1.verlaag_stock(3,5)
s1.verlaag_stock(2,5)
s1.verlaag_stock(5,1)
s1.print()
