# ADT Werknemer
## data
class Werknemer:
    def __init__(self):
        self.id = None #id van werknemer
        self.voornaam = None #voornaam werknemr
        self.achternaam = None #achternaam werknemer
        self.workload = None #workload werknemer uitgedrukt in credits

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
        info_werknemer = dict()
        info_werknemer[id] = voornaam,achternaam,workload

    def ontslag(self,id):
        """
        werknemer neemt ontslag en wordt verwijdert uit databank "info_werknemer"
        preconditie: werknemer moet in databank zijn
        postconditie: wordt verijdert uit databank
        :param id: unieke string
        :return: geeft niks terug
        """
        pass

