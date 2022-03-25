
output = "<html>"
rij = "<TABLE BORDER=1>"
for i in range(6):
    rij + "<TR>" + "<TD>" + "david" + "</TD>"
    output + rij
    rij = ""

output += "</html>"
hs = open("test.html",'w')
hs.write(output)