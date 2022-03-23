#thomas th maakt, Daan test
## functionaliteit

from binary_search_tree import BST
werknemers = BST()
class werknemer():

    def __init__(self,voornaam,achternaam,workload):
        self.voornaam = voornaam # nog geen id toegekend
        self.achternaam = achternaam # prijs is bekend
        self.workload = workload # vervaldatum is onbekend

    def add_werknemer(self,voornaam, achternaam, workload):

        werknemers.searchTreeInsert([achternaam,[voornaam,workload]])
        werknemers.inorderTraverse(print)
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

        #pass

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

        pass

w1 = werknemer("david","scalais",3)
w1.add_werknemer("david","scalais",3)
