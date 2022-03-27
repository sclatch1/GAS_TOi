# ADT Gebruiker
## data
from binary_search_tree import BST
class gebruikers:
    def __init__(self):
        self.gebruikers = BST()

### functionaliteit

    def voeg_gebruiker_toe(self, voornaam, achternaam, e_mailadress):
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

        self.gebruikers.searchTreeInsert([voornaam + " " + achternaam, e_mailadress])

    def verwijder_gebruiker(self, voornaam, achternaam):
        """
        verwijder een gebruiker van de ADT indien deze bestaat

        preconditie : voornaam en achternaam staan in de ADT
        postconditie : /

        : param voornaam : een string die de voornaam van de gebruiker
        voorstelt :
        : param achternaam : een string die de achternaam van de gebruiker
        voorstelt :
        : return : geeft niets terug
        """

        self.gebruikers.searchTreeDelete(voornaam + " " + achternaam)

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