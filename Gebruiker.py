# david en daan maakt, thomas th test
# ADT Gebruiker
## data
class Gebruiker:
    def __init__(self,e_mailadres, id, voornaam, achternaam):
        self.e_mailadres = e_mailadres # e_mailadres onbekend
        self.id = e_mailadres
        self.voornaam = voornaam # voornaam onbekend
        self.achternaam = achternaam # achternaam onbekend
        self.databank = dict()

### functionaliteit

    def voeg_gebruiker_toe(self,naam,voornaam,e_mailadress):
        """
        voeg een gebruiker toe aan de databank.
        gebruiker wordt opgezocht in databank via e_mailadres
        databank is een dictionary
        preconditie: naam,voornaam en e_mailadress zijn strings
        :param naam: een string die de naam van gebruiker voorstelt
        :param voornaam: een string die de voornaam van gebruiker voorstelt
        :param e_mailadress: een string die de e_mailadres van gebruiker voorstelt
        :return: geeft niets terug
        """
        pass

    def meld_aan(self):
        """
        check of een gebruiker in de databank is
        zoniet -> foutmelding
        zowel -> kan een bestelling plaatsen
        preconditie: id is een unieke string
        postconditie: kan een bestelling plaatsen
        :param id: e-mailadres van gebruiker
        :return: geeft niks terug
        """
        pass

    def meldt_af(self):
        """
        kan zich afmelden
        postconditie: moet eerst aangemeld zijn
        :param id: unieke string van gebruiker
        :return:
        """
        pass

    def betaalt_bestelling(self):
        """
        preconditie: moet een bestelling gemaakt hebben
        postconditie: kassa wordt verhoogt met geld van klant
        :param bestelling: bestelling van gebruiker
        :return: geeft niks terug
        """
        pass