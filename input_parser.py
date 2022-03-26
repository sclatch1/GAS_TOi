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
            if ("shot" in line):
                if ("melk" in line):
                    return

                if ("wit" in line):
                    return

                if ("zwart" in line):
                    return

                if ("bruin" in line):
                    return

            if ("honing" in line):
                return

            if ("marshmellow" in line):
                return

            if ("chili" in line):
                return

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