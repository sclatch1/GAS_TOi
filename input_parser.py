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
                    shop.vul_stock_aan(6,numbers[0], [numbers[1], numbers[2], numbers[3]])

                elif ("wit" in line):
                    shop.vul_stock_aan(3,numbers[0], [numbers[1], numbers[2], numbers[3]])

                elif ("zwart" in line):
                    shop.vul_stock_aan(5,numbers[0], [numbers[1], numbers[2], numbers[3]])

                elif ("bruin" in line):
                    shop.vul_stock_aan(4,numbers[0], [numbers[1], numbers[2], numbers[3]])

            elif ("honing" in line):
                shop.vul_stock_aan(0,numbers[0], [numbers[1], numbers[2], numbers[3]])

            elif ("marshmellow" in line):
                shop.vul_stock_aan(1,numbers[0], [numbers[1], numbers[2], numbers[3]])

            elif ("chili" in line):
                shop.vul_stock_aan(2,numbers[0], [numbers[1], numbers[2], numbers[3]])

            # vul werknemers en gebruikers aan
            elif ("werknemer" in line):
                words = line.split()
                shop.werknemer(words[1], words[2], words[3])

            elif ("gebruiker" in line):
                words = line.split()
                shop.gebruiker(words[1], words[2], words[3])

            # bestellingen
            elif ("bestel" in line):
                return

            # genereer output
            if ("log" in line):
                return
    return shop

input_parser("input_bestand.txt")