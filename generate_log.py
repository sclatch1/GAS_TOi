from Bestelling import Bestelling
from Stocks import Stocks
from Werknemer import werknemers
from Gebruiker import gebruikers
from arraybased_queue import MyQueue


class Output:
    def __init__(self):
        self.lijst = list()
        #["tijdstip", "stack", "naam", "Nieuwe bestellingen", "Wachtende bestellingen", "wit", "melk",
        #"zwart", "honing", "marshmallow", "chili"]
        self.tijdstippen = list()
        self.tijdstip = 1

    def generate_data(self, bestelling: Bestelling, stock: Stocks, werknemers: werknemers, gebruikers: gebruikers):
        # generate data voor het huidige tijdstip
        self.tijdstippen.append(list())
        self.lijst = list()

        # tijdstip
        self.tijdstippen[self.tijdstip - 1].append(self.tijdstip)
        self.lijst.append("tijdstip")

        # stack
        self.tijdstippen[self.tijdstip - 1].append("?")
        self.lijst.append("stack")

        # users (onbepaald aantal)
        y = 2
        werknemers_array = werknemers.werknemers_namen
        for x in werknemers_array:
            self.tijdstippen[self.tijdstip - 1].append(werknemers.werknemers.searchTreeRetrieve(x)[0])
            self.lijst.append(x)
            y += 1

        # nieuwe bestellingen
        self.tijdstippen[self.tijdstip - 1].append(len(bestelling.bestellingen.save()))
        self.lijst.append("Nieuwe bestellingen")

        # wachtende bestellingen
        self.tijdstippen[self.tijdstip - 1].append("?")
        self.lijst.append("Wachtende bestellingen")

        # wit
        self.tijdstippen[self.tijdstip - 1].append(len(stock.stock_shot_wit.save()))
        self.lijst.append("wit")

        # melk
        self.tijdstippen[self.tijdstip - 1].append(len(stock.stock_shot_melk.save()))
        self.lijst.append("melk")

        # zwart
        self.tijdstippen[self.tijdstip - 1].append(len(stock.stock_shot_zwart.save()))
        self.lijst.append("zwart")

        # honing
        self.tijdstippen[self.tijdstip - 1].append(len(stock.stock_honing.save()))
        self.lijst.append("honing")

        # marshmellow
        self.tijdstippen[self.tijdstip - 1].append(len(stock.stock_marshmellow.save()))
        self.lijst.append("marshmellow")

        # chili
        self.tijdstippen[self.tijdstip - 1].append(len(stock.stock_chili.save()))
        self.lijst.append("chili")


        self.tijdstip += 1

    def generate_html(self, naam):
        output = "<html>" + "<h1>Log</h1>"
        output += "<TABLE BORDER=1>"
        rowCounter = 0
        collumnCounter = 0
        # 1ste rij van tabel wordt aangemaakt met alle elementen van self.lijst
        rij = "<TR>"
        for item in self.lijst:
            rij += "<TD>" + item + "</TD>"
        rij += "</TR>"
        output += rij

        # rijen met data
        for tijdstip in self.tijdstippen:
            rij = "<TR>"
            for data in tijdstip:
                rij += "<TD>" + str(data) + "</TD>"
            rij += "</TR>"
            output += rij

        # tabel eindigt hier
        output += "</table> </html>"
        name_file = "log" + naam + ".html"
        hs = open(name_file, 'w')
        hs.write(output)

"""
out = Output()
out.generate_html("4")
"""