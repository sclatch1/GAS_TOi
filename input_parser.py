import QuetzalShop

# Leest text bestand en doet wat er staat
def input_parser(filename):
    # variablen
    shop = QuetzalShop

    # voer bestand uit
    file = open(filename, 'r')
    Lines = file.readlines()

    for line in Lines:
        if (line[0] != "#"):    # lijnen met '#' worden genegeerd
            print(line.strip())

            # initialiseer QuetzalShop
            if (line == "init"):
                shop = QuetzalShop

            # vul stock aan
            line = ''.join([i for i in line if not i.isalpha()])    # extract numbers
            numbers = line.split()
            if ("shot" in line):
                if ("melk" in line):
                    shop.QuetzalShop.vul_stock_aan(7,numbers[0])

                if ("wit" in line):
                    shop.QuetzalShop.vul_stock_aan(4,numbers[0])

                if ("zwart" in line):
                    shop.QuetzalShop.vul_stock_aan(6,numbers[0])

                if ("bruin" in line):
                    shop.QuetzalShop.vul_stock_aan(5,numbers[0])

            if ("honing" in line):
                shop.QuetzalShop.vul_stock_aan(1,numbers[0])

            if ("marshmellow" in line):
                shop.QuetzalShop.vul_stock_aan(2,numbers[0])

            if ("chili" in line):
                shop.QuetzalShop.vul_stock_aan(3,numbers[0])

            # vul werknemers en gebruikers aan
            if ("werknemer" in line):
                return

            if ("gebruiker" in line):
                return

            # bestellingen
            if ("bestel" in line):
                return

            # genereer output
            if ("log" in line):
                return


input_parser("7571236.txt")