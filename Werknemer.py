# functionaliteit

from binary_search_tree import BST
class werknemers():

    def __init__(self):
        self.werknemers = BST()

    def add_werknemer(self,voornaam, achternaam, workload):

        """
        voeg een werknemer toe aan de ADT indien deze nog niet bestaat

        preconditie : voornaam en achternaam zijn geldige namen, workload is positief integer
        postconditie : aantal_personeel gaat met 1 omhoog

        : param voornaam : een string die de voornaam van de werknemer
        voorstelt :
        : param achternaam : een string die de achternaam van de werknemer
        voorstelt :
        : param workload : een integer die de workload van de werknemer in credits
        voorstelt :
        : return : geeft niets terug
        """

        self.werknemers.searchTreeInsert([voornaam + " " + achternaam, workload])

    def verwijder_werknemer(self,voornaam, achternaam):
        """
        verwijder een werknemer van de ADT indien deze bestaat

        preconditie : voornaam en achternaam staan in de ADT
        postconditie : aantal_personeel gaat met 1 omlaag

        : param voornaam : een string die de voornaam van de werknemer
        voorstelt :
        : param achternaam : een string die de achternaam van de werknemer
        voorstelt :
        : return : geeft niets terug
        """

        self.werknemers.searchTreeDelete(voornaam + " " + achternaam)

