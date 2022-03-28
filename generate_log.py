from Bestelling import Bestelling
from Stocks import Stocks
from Werknemer import werknemers
from arraybased_queue import MyQueue


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
        data = []
        data += self.bestellingen.bestellingen.save()
        wit = self.stock.stock_shot_wit
        melk = self.stock.stock_shot_melk
        zwart = self.stock.stock_shot_zwart
        bruin = self.stock.stock_shot_bruin
        honing = self.stock.stock_honing
        marshmallow = self.stock.stock_marshmellow
        chili = self.stock.stock_chili
        for element in data:
            if 0 == 0:

                self.tijdstip_1 += " "
                self.tijdstip_1 += " "
                self.tijdstip_1 += " "
                self.tijdstip_1 += " "
                self.tijdstip_1 += len(wit.save)
                self.tijdstip_1 += len(melk.save())
                self.tijdstip_1 += len(zwart.save())
                self.tijdstip_1 += len(honing.save())
                self.tijdstip_1 += len(marshmallow.save())
                self.tijdstip_1 += len(chili.save())

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
        hs = open( self.name + ".html", 'w')
        hs.write(output)

