
output = "<html>" + "<h1>LOG</h1>"
output += "<TABLE BORDER=1>"

lijst = ["tijdstip","stack","naam","Nieuwe bestellingen","Wachtende bestellingen","wit","melk","zwart","honing","marshmallow","chili"]

counter = 0
for i in range(6):
    eersterij = "<TR>"
    rij = "</TR>"
    for item in lijst:
        if counter == 0:
            eersterij += "<TD>" + item + "</TD>"
        else:
            rij += "<TD>" + "</TD>"
    rij += "</TR>"
    eersterij += "</TR>"
    if counter == 0:
        output += eersterij
    else:
        output += rij
    counter += 1

output += "</table> </html>"
hs = open("log4.html", 'w')
hs.write(output)