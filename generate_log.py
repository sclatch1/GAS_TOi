from Bestelling import Bestelling
from Stocks import Stocks
from Werknemer import werknemers
from Gebruiker import gebruikers
from arraybased_queue import MyQueue


class Output:
    def __init__(self):
        self.lijst = ["tijdstip", "stack", "naam", "Nieuwe bestellingen", "Wachtende bestellingen", "wit", "melk",
                      "zwart", "honing", "marshmallow", "chili"]
        self.tijdstippen = []
        self.tijdstip = 1

    def generate_data(self, bestelling: Bestelling, stock: Stocks, werknemers: werknemers, gebruikers: gebruikers):
        # generate data voor het huidige tijdstip

        # tijdstip
        self.tijdstippen[self.tijdstip-1] = [self.tijdstip]

        # stack
        self.tijdstippen[self.tijdstip - 1][1] = "?"

        # users (onbepaald aantal)


        # nieuwe bestellingen


        # wachtende bestellingen


        # stock (7)


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
        rij = "<TR>"
        for element in self.tijdstip_1:
            rij += "<TD>" + str(element) + "</TD>"
        rij += "</TR>"
        output += rij
        for element in self.tijdstip_2:
            rij += "<TD>" + str(element) + "</TD>"
        rij += "</TR>"
        output += rij
        for element in self.tijdstip_3:
            rij += "<TD>" + str(element) + "</TD>"
        rij += "</TR>"
        output += rij
        for element in self.tijdstip_4:
            rij += "<TD>" + str(element) + "</TD>"
        rij += "</TR>"
        output += rij

        # tabel eindigt hier
        output += "</table> </html>"
        hs = open("log" + naam + ".html", 'w')
        hs.write(output)
