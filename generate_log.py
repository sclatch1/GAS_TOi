from Bestelling import Bestelling
from Stocks import Stocks
from Werknemer import werknemers
from arraybased_queue import MyQueue


class Output:
    def __init__(self):
        self.lijst = ["tijdstip", "stack", "naam", "Nieuwe bestellingen", "Wachtende bestellingen", "wit", "melk",
                      "zwart", "honing", "marshmallow", "chili"]
        self.tijdstippen = []
        self.tijdstip = 1

    def generate_data(self, bestelling: Bestelling, stock: Stocks, werknemers: werknemers):
        # generate data voor het huidige tijdstip
        pass

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