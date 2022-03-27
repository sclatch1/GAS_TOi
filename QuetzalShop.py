# ADT QuetzalShop
## data
import Stocks
import Werknemer
import Gebruiker
import generate_log
from Bestelling import Bestelling


class QuetzalShop:
    def __init__(self):
        self.stock = Stocks.Stocks()  # stock klasse : product, aantal en vervaldatum
        self.bestellingen = Bestelling()  # dictionary van bestellingen: bestelling en prijs
        self.werknemers = Werknemer.werknemers()  # werknemers klasse: bewaard werknemers
        self.gebruikers = Gebruiker.gebruikers()  # gebruiker klasse: bewaard gebruikers

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

    def output(self):
        """
        :return: output gegevens in html bestand
        """
        log = generate_log.Output(self)
        log.generate_html()

    def verwerk_bestelling(self, bestelling, werknemer):
        """
        verwerkt een bestelling door een werknemer via credit systeem.
        voor verwerking wordt bestelling en werknemer voorgesteld als credit
        preconditie: bestelling en werknemer is een integer die crediten voorstelt
        :param bestelling: aantal credit
        :param werknemer: aantal credit die een werknemer kan verwerken
        :return: geeft niets terug
        """
        pass

    def verhoog_kassa(self, prijs_bestelling):
        """
        krijgt geld verschuldig van gebruiker voor bestelling
        preconditie: een integer
        postconditie: geld in kassa wordt verhoogt met prijs bestelling
        :param prijs_bestelling: is een integer van de prijs
        :return: geeft niks terug
        """
        pass

    def verlaag_kassa(self, salaries, stocks):
        """
        verlaag kassa met prijs van stockaanvulling en salaries toegekend.
        preconditie: genoeg geld in kassa
        postconditie: kassa wordt verlaagt met prijs
        :param salaries: een integer
        :param stocks: een integer
        :return: geeft niks terug
        """
        pass

    def betaalt_salaries(self, werknemer, salaries):
        """
        werknemers ontvangen salaries
        preconditie: salaries is een integer
        postconditie: kassa wordt verlaagt met salaries
        :param werknemer: id_werknemer
        :param salaries: integer
        :return: geeft niks terug
        """
        pass
