from QuetzalShop import QuetzalShop


# Leest text bestand en doet wat er staat
def input_parser(filename):
    # variablen
    shop = QuetzalShop()

    # voer bestand uit
    file = open(filename, 'r')
    Lines = file.readlines()

    for line in Lines:
        if (line[0] != "#"):  # lijnen met '#' worden genegeerd
            print(line.strip())

            # initialiseer QuetzalShop
            if (line == "init\n"):
                shop = QuetzalShop()

            # vul stock aan
            tempnumbers = ''.join([i for i in line if not i.isalpha()])  # extract numbers
            numbers = tempnumbers.split()
            if ("shot" in line):
                if ("melk" in line):
                    shop.stock.vul_stock_aan(0, int(numbers[0]))

                elif ("wit" in line):
                    shop.stock.vul_stock_aan(4, int(numbers[0]))

                elif ("zwart" in line):
                    shop.stock.vul_stock_aan(6, int(numbers[0]))

                elif ("bruin" in line):
                    shop.stock.vul_stock_aan(5, int(numbers[0]))

            elif ("honing" in line):
                shop.stock.vul_stock_aan(1, int(numbers[0]))

            elif ("marshmellow" in line):
                shop.stock.vul_stock_aan(2, int(numbers[0]))

            elif ("chili" in line):
                shop.stock.vul_stock_aan(3, int(numbers[0]))

            # vul werknemers en gebruikers aan
            elif ("werknemer" in line):
                return

            elif ("gebruiker" in line):
                return

            # bestellingen
            elif ("bestel" in line):
                return

            # genereer output
            if ("log" in line):
                return
    return shop

print(type(input_parser("input_bestand.txt")))


#print(type(stock))



#print(stock.print())