from Bestelling import Bestelling
from QuetzalShop import QuetzalShop

class Output:
    def __init__(self, bestellingen: Bestelling, name):
        self.lijst = ["tijdstip", "stack", "naam", "Nieuwe bestellingen", "Wachtende bestellingen", "wit", "melk",
                      "zwart", "honing", "marshmallow", "chili"]
        self.tijdstip_1 = [0]
        self.tijdstip_2 = [1]
        self.tijdstip_3 = [2]
        self.tijdstip_4 = [3]
        self.tijdstip_5 = [4]
        self.bestellingen = bestellingen
        self.name = name

    def generate_html(self):
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
        for element in self.tijdstip_1:
            rij += "<TD>" + item + "</TD>"
        rij += "</TR>"
        output += rij

        # tabel eindigt hier
        output += "</table> </html>"
        hs = open("log" + self.name + ".html", 'w')
        hs.write(output)

