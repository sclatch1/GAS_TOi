#thomas g en daan maakt, david test
# ADT QuetzalShop
## data

class QuetzalShop:
    def __init__(self):
        self.stock = dict()          # dictionary van de stock: product en aantal
        self.bestellingen = dict()   # dictionary van bestellingen: bestelling en prijs
        self.kassa = 0               # het geld in de kassa
        pass
### functionaliteit

    def werknemer(self,id, voornaam, achternaam, workload):
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
        pass

    def vul_stock_aan(self,product, aantal):
        """
        vul stock aan met chocolademelk, wit chocolade shot, bruin chocolade shot, zwart chocolade shot, honing, marshmallow, chilipeper
        preconditie: een integer 0,1,2,3,4,5,6 voor product en een integer voor aantal
        postconditie: stock wordt verhoogt met aantal van elk product en kassa wordt verlaagt.
        :param
        aantal: aantal te vullen producten
        product: een integer 0,1,2,3,4,5,6,7 die elk een product voorstelt:
        0 = chocolademelk
        1 = honing
        2 = marshmallow
        3 = chilipeper
        4 = wit chocolade shot
        5 = bruin chocolade shot
        6 = zwart chocolade shot
        7 = melk shot
        :return: geeft niks terug
        """

        if product == 0:
            self.stock["chocolademelk"] += aantal
        if product == 1:
            self.stock["honing"] += aantal
        if product == 2:
            self.stock["marshmallow"] += aantal
        if product == 3:
            self.stock["chilipeper"] += aantal
        if product == 4:
            self.stock["wit chocolade shot"] += aantal
        if product == 5:
            self.stock["bruin chocolade shot"] += aantal
        if product == 6:
            self.stock["zwart chocolade shot"] += aantal
        if product == 7:
            self.stock["melk shot"] += aantal


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
        if aantal == 0:
            self.stock["chocolademelk"] -= aantal
        if aantal == 1:
            self.stock["honing"] -= aantal
        if aantal == 2:
            self.stock["marshmallow"] -= aantal
        if aantal == 3:
            self.stock["chilipeper"] -= aantal
        if aantal == 4:
            self.stock["wit chocolade shot"] -= aantal
        if aantal == 5:
            self.stock["bruin chocolade shot"] -= aantal
        if aantal == 6:
            self.stock["zwart chocolade shot"] -= aantal

    def voeg_chocolade_toe (self,chocoladeshot) :

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

        if self.chocoladeshot == 0 and "wit chocolade shot" in self.stock:
            self.stock["wit chocolade shot"] += 1
        else:
            self.stock["wit chocolade shot"] = 1
        if chocoladeshot == 1 and "melk chocolade shot" in self.stock:
            self.stock["melk chocolade shot"] += 1
        else:
            self.stock["melk chocolade shot"] = 1
        if chocoladeshot == 2 and "bruin chocolade shot" in self.stock:
            self.stock["bruin chocolade shot"] += 1
        else:
            self.stock["bruin chocolade shot"] = 1
        if chocoladeshot == 3 and "zwart chocolade shot" in self.stock:
            self.stock["zwart chocolade shot"] += 1
        else:
            self.stock["zwart chocolade shot"] = 1

    def voeg_honing_toe(self):
        """
        voeg honing toe aan de chocolademelk
        preconditie: geen preconditie
        postconditie: de prijs van de chocolademelk is verhoogd met 0,50 EUR
        :return: geeft niets terug
        """

        if "honing" in self.stock:
            self.stock["honing"] += 1
        else:
            self.stock["honing"] = 1

    def voeg_marshmallow_toe(self):
        """
        voeg marshmallow toe aan de chocolademelk
        preconditie: geen preconditie
        postconditie: de prijs van de chocolademelk is verhoogd met 0,75 EUR
        :return: geeft niets terug
        """
        if "marshmallow" in self.stock:
            self.stock["marshmallow"] += 1
        else:
            self.stock["marshmallow"] = 1

    def voeg_chilipeper_toe(self):
        """
        voeg chilipeper toe aan de chocolademelk
        preconditie: geen preconditie
        postconditie: de prijs van de chocolademelk is verhoogd met 0,25 EUR
        :return: geeft niets terug
        """
        if "chilipeper" in self.stock:
            self.stock["chilipeper"] += 1
        else:
            self.stock["chilipeper"] = 1

    def verwerkt_bestelling(self,bestelling, werknemer):
        """
        verwerkt een bestelling door een werknemer via credit systeem.
        voor verwerking wordt bestelling en werknemer voorgesteld als credit
        preconditie: bestelling en werknemer is een integer die crediten voorstelt
        :param bestelling: aantal credit
        :param werknemer: aantal credit die een werknemer kan verwerken
        :return: geeft niets terug
        """
        pass

    def verhoog_kassa(self,prijs_bestelling):
        """
        krijgt geld verschuldig van gebruiker voor bestelling
        preconditie: een integer
        postconditie: geld in kassa wordt verhoogt met prijs bestelling
        :param prijs_bestelling: is een integer van de prijs
        :return: geeft niks terug
        """
        del self.bestelling["bestelling"]
        self.kassa += prijs_bestelling

    def verlaag_kassa(self,salaries,stocks):
        """
        verlaag kassa met prijs van stockaanvulling en salaries toegekend.
        preconditie: genoeg geld in kassa
        postconditie: kassa wordt verlaagt met prijs
        :param salaries: een integer
        :param stocks: een integer
        :return: geeft niks terug
        """
        pass

    def betaalt_salaries(self,werknemer, salaries):
        """
        werknemers ontvangen salaries
        preconditie: salaries is een integer
        postconditie: kassa wordt verlaagt met salaries
        :param werknemer: id_werknemer
        :param salaries: integer
        :return: geeft niks terug
        """
        pass