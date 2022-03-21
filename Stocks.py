# thomas g en david maakt, daan test
# ADT Stocks
## data
class Stocks:
    def __init__(self):
        self.chocoladeshots = [None] #aantal niet gekend
        self.honingsporties = [None] #aantal niet gekend
        self.marshmallows = [None] #aantal niet gekend
        self.chilipeperporties = [None] #aantal niet gekend

### functionaliteit

    def verlaag_stock(self,product, aantal):
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
        pass

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
        pass

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