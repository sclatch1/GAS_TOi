#david en thomas th maakt, thomas g test
# ADT Bestelling
## data
class Bestelling:
    def __init__(self):
        self.id = None  # nog geen id toegekend
        self.id_gebruiker = None  # email_adres in ADT Gebruiker
        self.timestamp = None  # een timestamps met tijd en datum
        self.id_chocolademelk = None  # id in ADT chocolademelk
        self.bestellingen = dict()

    ### functionaliteit
    def order(self, id_gebruiker, id_chocolademelk, afgehaald):
        """
        Houd bestellingen bij in een dictionary.
        preconditie: id_gebruiker en id_chocolademelk zijn strings, afgehaald een integer uit 0,1
        postconditie : bestelling wordt toegevoegd aan bestellingen
        :param id_gebruiker: een unieke string die wordt toegekend aan een gebruiker
        :param id_choclademelk: een unieke string die wordt toegekend aan een chocolademelk
        :param afgehaald: een integer die laat zien of een bestelling is afgehaald of niet.
        O = afgehaald
        1 = niet afgehaald
        :return: geeft een dictionary met bestellingen terug
        """
        pass

    def annuleert_bestelling(self, id_gebruiker, id_chocolademelk, bestellingen):
        """
        annuleert bestelling van id_gebruiker en verwijdert uit de databank: "bestellingen".
        preconditie: id_gebruiker moet in databank "accounts" zijn en bestelling moet in databank "bestellingen zijn"
        postconditie: bestelling wordt verwijdert uit databank "bestellingen"
        :param id_gebruiker: unieke string
        :param id_chocolademelk: uinieke string
        :param bestellingen: databank met bestellingen
        :return: geeft niks terug
        """
        pass