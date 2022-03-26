# thomas g en david maakt, daan test
# ADT Stocks
## data
from Chilipeper import Chilipeper
from Chocolademelk import Chocolademelk
from Chocoladeshot import Chocoladeshot
from Marshmallow import Marshmallow
from Honing import Honing

class Stocks:
    def __init__(self):
        choco = Chocoladeshot()
        marsh = Marshmallow()
        hon = Honing()
        chili = Chilipeper()
        self.marshmallows = [marsh,0]
        self.chocolademelk = [choco,0]
        self.wit_chocolade_shot = [choco,0]
        self.bruin_chocolade_shot = [choco,0]
        self.zwart_chocolade_shot = [choco,0]
        self.honing = [hon,0]
        self.chilipeper = [chili,0]
        self.stock = [self.chocolademelk,self.honing,self.marshmallows,self.chilipeper,self.wit_chocolade_shot,self.bruin_chocolade_shot,self.zwart_chocolade_shot]

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
            self.stock[product][1] -= aantal
            if(self.stock[product][1] < 0):
                self.stock[product][1] = 0
        elif product == 1:
            self.stock[product][1] -= aantal
            if (self.stock[product][1] < 0):
                self.stock[product][1] = 0
        elif product == 2:
            self.stock[product][1] -= aantal
            if (self.stock[product][1] < 0):
                self.stock[product][1] = 0
        elif product == 3:
            self.stock[product][1] -= aantal
            if (self.stock[product][1] < 0):
                self.stock[product][1] = 0
        elif product == 4:
            self.stock[product][1] -= aantal
            if (self.stock[product][1] < 0):
                self.stock[product][1] = 0
        elif product == 5:
            self.stock[product][1] -= aantal
            if (self.stock[product][1] < 0):
                self.stock[product][1] = 0
        elif product == 6:
            self.stock[product][1] -= aantal
            if (self.stock[product][1] < 0):
                self.stock[product][1] = 0
        #if self.honing < 0 or self.zwart_chocolade_shot < 0 or self.bruin_chocolade_shot < 0 or self.wit_chocolade_shot < 0 or self.chocolademelk < 0 or self.chilipeper < 0 or self.marshmallows < 0:
        #for ingredient in self.stock:
        #    if ingredient < 0:
        #        ingredient = 0
        else:
            print("inkopen")
        print(self.stock)

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
            self.stock[product][1] += aantal
        elif product == 1:
            self.stock[product][1] += aantal
        elif product == 2:
            self.stock[product][1] += aantal
        elif product == 3:
            self.stock[product][1] += aantal
        elif product == 4:
            self.stock[product][1] += aantal
        elif product == 5:
            self.stock[product][1] += aantal
        elif product == 6:
            self.stock[product][1] += aantal
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
        for product in self.stock:
            if product.vervaldatum < timestamp:
                product[1] = 0

    def print(self):
        output = " chocolademelk: " + str(self.chocolademelk[1]) + " honing: " + str(self.honing[1]) + " chili: " + str(self.chilipeper[1]) + " marshmallow: " + str(self.marshmallows[1]) + " wit: " + str(self.wit_chocolade_shot[1])
        output += " zwart: " + str(self.zwart_chocolade_shot[1]) + " bruin: " + str(self.bruin_chocolade_shot[1])
        return output


"""
s1 = Stocks()
s1.vul_stock_aan(2,8)
s1.vul_stock_aan(5,8)
s1.vul_stock_aan(9,8)
s1.vul_stock_aan(0,8)


s1.verlaag_stock(2,5)
s1.verlaag_stock(5,1)

"""