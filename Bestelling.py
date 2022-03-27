# david en thomas th maakt, thomas g test
# ADT Bestelling
## data
from arraybased_queue import MyQueue
from Chocolademelk import Chocolademelk
import Stocks


class Bestelling:
    def __init__(self):
        self.bestellingen = MyQueue(100)
        self.timestamps = dict()

    ### functionaliteit
    def order(self, tijdstip, tijd, ingredienten, email, stock: Stocks.Stocks):
        """
        Houd bestellingen bij in een queue.
        preconditie: id_gebruiker en id_chocolademelk zijn strings, afgehaald een integer uit 0,1
        postconditie : bestelling wordt toegevoegd aan bestellingen
        :param tijdstip: een cijfer dat het tijdstip aanduid
        :param tijd: de tijd die bij het tijdstip hoort
        :param ingredienten: een array van ingredienten (0-6)
        :param email: email van de gebruiker
        :param stock: de stock van de winkel
        :return: geeft niks terug
        """

        self.timestamps[tijdstip] = tijd

        bestelling = Chocolademelk()

        for x in ingredienten:
            if x == 0:
                bestelling.voeg_honing_toe()
                stock.verlaag_stock(0, 1)

            elif x == 1:
                bestelling.voeg_marshmallow_toe()
                stock.verlaag_stock(1, 1)

            elif x == 2:
                bestelling.voeg_chilipeper_toe()
                stock.verlaag_stock(2, 1)

            elif x == 3:
                bestelling.voeg_chocolade_toe(0)
                stock.verlaag_stock(3, 1)

            elif x == 4:
                bestelling.voeg_chocolade_toe(1)
                stock.verlaag_stock(4, 1)

            elif x == 5:
                bestelling.voeg_chocolade_toe(2)
                stock.verlaag_stock(5, 1)

            elif x == 6:
                bestelling.voeg_chocolade_toe(3)
                stock.verlaag_stock(6, 1)

        self.bestellingen.enqueue([tijdstip, email, bestelling])

    def annuleert_bestelling(self, email):
        """
        annuleert bestelling van id_gebruiker en verwijdert uit de databank: "bestellingen".
        preconditie: id_gebruiker moet in databank "accounts" zijn en bestelling moet in databank "bestellingen zijn"
        postconditie: bestelling wordt verwijdert uit databank "bestellingen"
        :param id_gebruiker: unieke string
        :param id_chocolademelk: uinieke string
        :param bestellingen: databank met bestellingen
        :return: geeft niks terug
        """

        return
