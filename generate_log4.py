
output = "<html>"
output += "<TABLE BORDER=1>"
for i in range(6):
    rij = "<TR>"
    for j in range(7):
        rij += "<TD>" + "melk" + "</TD>"
    rij += "</TR>"
    output += rij
output += "</table> </html>"
hs = open("test.html",'w')
hs.write(output)