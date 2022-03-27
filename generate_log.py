
class Output:
    def __init__(self, shop):
        self.lijst = ["tijdstip","stack","naam","Nieuwe bestellingen","Wachtende bestellingen","wit","melk","zwart","honing","marshmallow","chili"]
        self.tijdstip_1 = []
        self.tijdstip_2 = []
        self.tijdstip_3 = []
        self.tijdstip_4 = []
        self.tijdstip_5 = []
        self.tijdstip_6 = []
        self.shop = shop

    def generate_html(self):
        output = "<html>" + "<h1>Log</h1>"
        output += "<TABLE BORDER=1>"
        rowCounter = 0
        collumnCounter = 0
        # 1ste rij van tabel wordt aangemaakt met alle elementen van self.lijst
        eersterij = "<TR>"
        for item in self.lijst:
            eersterij += "<TD>" + item + "</TD>"
        eersterij += "</TR>"
        output += eersterij

        #tabel eindigt hier
        output += "</table> </html>"
        hs = open("log4.html", 'w')
        hs.write(output)