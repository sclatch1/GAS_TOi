
output = "<html>" + "<h1>Log</h1>"
output += "<TABLE BORDER=1>"

lijst = ["tijdstip","stack","naam","Nieuwe bestellingen","Wachtende bestellingen","wit","melk","zwart","honing","marshmallow","chili"]

rowCounter = 0
collumnCounter = 0
for i in range(6):
    eersterij = "<TR>"
    rij = "</TR>"
    for item in lijst:
        if rowCounter == 0:
            eersterij += "<TD>" + item + "</TD>"
        elif rowCounter > 0 and collumnCounter == 0:
            rij += "<TD>" + str(rowCounter) + "</TD>"
        else:
            rij += "<TD>" + "</TD>"
        collumnCounter += 1
    collumnCounter = 0
    rij += "</TR>"
    eersterij += "</TR>"
    if rowCounter == 0:
        output += eersterij
    else:
        output += rij
    rowCounter += 1


output += "</table> </html>"
hs = open("log4.html", 'w')
hs.write(output)