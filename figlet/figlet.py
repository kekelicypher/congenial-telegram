from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
fonts = figlet.getFonts()

if len(sys.argv) < 2:
    font = random.choice(fonts)
    print(font)

    figlet.setFont(font=font)

    input = input("Enter some text: ")
    print(figlet.renderText(input))

elif (len(sys.argv) > 2) and (sys.argv[1] in ["-f", "--font"]):
    figlet.setFont(font=sys.argv[2])

    input = input("Enter some text: ")
    print(figlet.renderText(input))

else:
    sys.exit("Invalid usage")
