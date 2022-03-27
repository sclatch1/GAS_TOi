


class Output:
    def __init__(self, bestelling, stock, werknemers):
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


    def generate_data(self):
        data = []
        for element in self.stock:
            print("test")

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


        # tabel eindigt hier
        output += "</table> </html>"
        hs = open( "log4" + ".html", 'w')
        hs.write(output)


