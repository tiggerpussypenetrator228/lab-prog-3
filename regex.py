import re

filename = input("Enter filename: ")

file = open(filename, "r", encoding="utf-8")
text = file.read()
file.close()

links = re.findall(r'\"(http|https):\/\/([\.a-zA-Z0-9%\-+\_]+)[\/|\"]([\/a-zA-Z0-9%\-+\_\.\&\?]+)?', string=text)
for link in links:
    protocol = link[0]
    domain = link[1]
    path = link[2]

    print("%s://%s/%s" % (protocol, domain, path))
