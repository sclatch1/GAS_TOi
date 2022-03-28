# ADT QuetzalShop
## data
import Stocks
import Werknemer
import Gebruiker
from generate_log import Output
from Bestelling import Bestelling


class QuetzalShop:
    def __init__(self):
        self.stock = Stocks.Stocks()  # stock klasse : product, aantal en vervaldatum
        self.bestellingen = Bestelling()  # dictionary van bestellingen: bestelling en prijs
        self.werknemers = Werknemer.werknemers()  # werknemers klasse: bewaard werknemers
        self.gebruikers = Gebruiker.gebruikers()  # gebruiker klasse: bewaard gebruikers
        self.log = Output()

    ### functionaliteit

    def werknemer(self, voornaam, achternaam, workload):
        """
        Houd een dictionary van informatie over een werknemer bij
        preconditie = id, voornaam, achternaam zijn strings
        workload een integer van 3 of 10
        postconditie = informatie werknemer wordt toegevoegs aan info_werknemer
        :param id: een unieke id van de werknemer
        :param voornaam: voornaam van werknemer
        :param achternaam: achternaam van werknemer
        :param workload: een integer van 10 of 3 die workload van
        een werknemer uitdrukt in credits.
        10 = 10 credits/tijdseenheid -> ervaren werknemer
        3 = 3 credits/tijdseenheid -> student werknemer
        :return: geeft niks terug
        """

        self.werknemers.add_werknemer(voornaam, achternaam, workload)

    def gebruiker(self, voornaam, achternaam, email):
        """
        Houd een dictionary van informatie over een gebruiker bij
        preconditie = email, voornaam, achternaam zijn strings
        postconditie = informatie gebruiker wordt toegevoegs aan de ADT
        :param voornaam: voornaam van gebruiker
        :param achternaam: achternaam van gebruiker
        :param email: email van gebruiker
        :return: geeft niks terug
        """

        self.gebruikers.voeg_gebruiker_toe(voornaam, achternaam, email)

    def vul_stock_aan(self, product, aantal, vervaldatum):
        """
        vul stock aan met chocolademelk, wit chocolade shot, bruin chocolade shot, zwart chocolade shot, honing, marshmallow, chilipeper
        preconditie: een integer 0,1,2,3,4,5,6 voor product en een integer voor aantal
        postconditie: stock wordt verhoogt met aantal van elk product en kassa wordt verlaagt.
        :param
        aantal: aantal te vullen producten
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

        self.stock.vul_stock_aan(product, aantal, vervaldatum)

    def verlaag_stock(self, product, aantal):
        """
            verlaag stock aan met chocolademelk, wit chocolade shot, bruin chocolade shot, zwart chocolade shot, honing, marshmallow, chilipeper
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

        self.stock.verlaag_stock(product, aantal)

    def bestelling(self, tijdstip, tijd, ingredienten, email):
        """
        voeg bestelling toe
        preconditie: alle nodige variablen
        postconditie: bestelling toegevoegd aan ADT
        :return: geeft niks terug
        """

        self.bestellingen.order(tijdstip, tijd, ingredienten, email, self.stock)

    def output(self,naam):
        """
        :return: output gegevens in html bestand
        """
        self.log.generate_html(naam)

    def generate_data(self):
        """
        :return: output gegevens in log
        """
        self.log.generate_data(self.bestellingen, self.stock, self.werknemers)

shop = QuetzalShop()
shop.output("4")