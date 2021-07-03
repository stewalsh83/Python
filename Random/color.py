import sys


for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[48;5;" + code + "m " + code.ljust(4))
    print(u"\u001b[0m")

for i in range(0, 16):
    for j in range(0, 16):
        code = str(i * 16 + j)
        sys.stdout.write(u"\u001b[38;5;" + code + "m " + code.ljust(4))
    print(u"\u001b[0m")

cd = {
    "black":"\u001b[30;1m",
    "red": "\u001b[31;1m",
    "green":"\u001b[32m",
    "yellow":"\u001b[33;1m",
    "blue":"\u001b[34;1m",
    "magenta":"\u001b[35m",
    "cyan": "\u001b[36m",
    "white":"\u001b[37m",
    "yellow-background":"\u001b[43m",
    "black-background":"\u001b[40m",
    "cyan-background":"\u001b[46;1m",
}
#You can add more colors and backgrounds to the dictionary if you like.


def colors(text):
    for c in cd:
        text = text.replace("[[" + c + "]]", cd[c])
    return text

print('\n')
# Example printing out some text
py = "[[blue]]Pyt[[yellow]]hon[[white]]"
print(colors(py))
print('\n')

# Example printing out an ASCII file
# Big Python Logo
f = open("pythonlogo.txt","r")
ascii = "".join(f.readlines())
print('{}'.format(colors(ascii)))

print('\n')
print(colors('[[magenta]]Hello World'))