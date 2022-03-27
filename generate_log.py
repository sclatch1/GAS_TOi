from Bestelling import Bestelling
from Stocks import Stocks
from Werknemer import werknemers


class Output:
    def __init__(self, bestelling: Bestelling, stock: Stocks, werknemers: werknemers,naam):
        self.lijst = ["tijdstip", "stack", "naam", "Nieuwe bestellingen", "Wachtende bestellingen", "wit", "melk",
                      "zwart", "honing", "marshmallow", "chili"]
        self.tijdstip_1 = [0]
        self.tijdstip_2 = [1]
        self.tijdstip_3 = [2]
        self.tijdstip_4 = [3]
        self.tijdstip_5 = [4]
        self.bestellingen = bestelling
        self.werknemers = werknemers
        self.stock = stock
        self.name = naam


    def generate_data(self):
        data = self.bestellingen.bestellingen.save()
        for element in data:
            if element[0] == 1:
                self.tijdstip_1 += "hey"
        print(self.tijdstip_1,"test")
        print(data)
    #)



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
        hs = open( "log" + self.name + ".html", 'w')
        hs.write(output)

