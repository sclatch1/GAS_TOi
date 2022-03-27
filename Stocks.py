# thomas g en david maakt, daan test
# ADT Stocks
## data
from Chilipeper import Chilipeper
from Chocoladeshot import Chocoladeshot
from Marshmallow import Marshmallow
from Honing import Honing
import arraybased_queue
from datetime import date

def days_calculator(date1, date2):
    # berekent tijd tussen 2 datums

    d0 = date(date1[0], date1[1], date1[2])
    d1 = date(date2[0], date2[1], date2[2])

    return d1 - d0

class Stocks:
    def __init__(self):
        # elke stock opgeslagen in een aparte queue
        self.stock_chili = arraybased_queue.MyQueue(100)
        self.stock_marshmellow = arraybased_queue.MyQueue(100)
        self.stock_honing = arraybased_queue.MyQueue(100)
        self.stock_shot_melk = arraybased_queue.MyQueue(100)
        self.stock_shot_wit = arraybased_queue.MyQueue(100)
        self.stock_shot_zwart = arraybased_queue.MyQueue(100)
        self.stock_shot_bruin = arraybased_queue.MyQueue(100)

    ### functionaliteit

    def vul_stock_aan(self, product, aantal, vervaldatum):
        """
        vul stock aan met chocolademelk, wit chocolade shot, bruin chocolade shot, zwart chocolade shot, honing, marshmallow, chilipeper
        preconditie: een integer 0,1,2,3,4,5,6 voor product en een integer voor aantal
        postconditie: stock wordt verhoogt met aantal van elk product en kassa wordt verlaagt.
        :param
        aantal: aantal te vullen producten
        vervaldatum: tijdstip wanneer het product vervalt (array)
        product: een integer 0,1,2,3 die elk een product voorstelt:
        0 = honing
        1 = marshmallow
        2 = chilipeper
        3 = wit chocolade shot
        4 = bruin chocolade shot
        5 = zwart chocolade shot
        6 = melk chocolade shot
        :return: geeft niks terug
        """

        if (product == 0):
            for x in range(int(aantal)):
                self.stock_honing.enqueue(Honing(vervaldatum))

        elif (product == 1):
            for x in range(int(aantal)):
                self.stock_marshmellow.enqueue(Marshmallow(vervaldatum))

        elif (product == 2):
            for x in range(int(aantal)):
                self.stock_chili.enqueue(Chilipeper(vervaldatum))

        elif (product == 3):
            for x in range(int(aantal)):
                self.stock_shot_wit.enqueue(Chocoladeshot(0, vervaldatum))

        elif (product == 4):
            for x in range(int(aantal)):
                self.stock_shot_bruin.enqueue(Chocoladeshot(1, vervaldatum))

        elif (product == 5):
            for x in range(int(aantal)):
                self.stock_shot_zwart.enqueue(Chocoladeshot(2, vervaldatum))

        elif (product == 6):
            for x in range(int(aantal)):
                self.stock_shot_melk.enqueue(Chocoladeshot(3, vervaldatum))

    def verlaag_stock(self, product, aantal):
        """
        verlaag stock van chocolademelk, wit chocolade shot, bruin chocolade shot, zwart chocolade shot, honing, marshmallow, chilipeper
        preconditie: een integer 0,1,2,3,4,5,6
        postconditie: stock wordt verlaag met aantal van elk product
        :param
        aantal: aantal te verlagen producten
        product: een integer 0,1,2,3 die elk een product voorstelt:
        0 = honing
        1 = marshmallow
        2 = chilipeper
        3 = wit chocolade shot
        4 = bruin chocolade shot
        5 = zwart chocolade shot
        6 = melk chocolade shot
        :return: geeft niks terug
        """
        if (product == 0):
            for x in range(aantal):
                self.stock_honing.dequeue()

        elif (product == 1):
            for x in range(aantal):
                self.stock_marshmellow.dequeue()

        elif (product == 2):
            for x in range(aantal):
                self.stock_chili.dequeue()

        elif (product == 3):
            for x in range(aantal):
                self.stock_shot_wit.dequeue()

        elif (product == 4):
            for x in range(aantal):
                self.stock_shot_bruin.dequeue()

        elif (product == 5):
            for x in range(aantal):
                self.stock_shot_zwart.dequeue()

        elif (product == 6):
            for x in range(aantal):
                self.stock_shot_melk.dequeue()

    def controle_verval_datum(self, timestamp):
        """
        controleert of vervaldatum van een product voor timestamp komt en verwijderd vervallen producten.
        preconditie: product is een integer, timestamp een een array in de vorm van [jaar, maand, dag]
        postcoditie: stock wordt verlaagt
        :param
        timestamp: huidige datum
        :return: geeft niks terug
        """

        while days_calculator(self.stock_honing.getFront().vervaldatum, timestamp) < 0:
            self.stock_honing.dequeue()

        while days_calculator(self.stock_marshmellow.getFront().vervaldatum, timestamp) < 0:
            self.stock_marshmellow.dequeue()

        while days_calculator(self.stock_chili.getFront().vervaldatum, timestamp) < 0:
            self.stock_chili.dequeue()

        while days_calculator(self.stock_shot_wit.getFront().vervaldatum, timestamp) < 0:
            self.stock_shot_wit.dequeue()

        while days_calculator(self.stock_shot_bruin.getFront().vervaldatum, timestamp) < 0:
            self.stock_shot_bruin.dequeue()

        while days_calculator(self.stock_shot_zwart.getFront().vervaldatum, timestamp) < 0:
            self.stock_shot_zwart.dequeue()

        while days_calculator(self.stock_shot_melk.getFront().vervaldatum, timestamp) < 0:
            self.stock_shot_melk.dequeue()


    def print(self):
        return

