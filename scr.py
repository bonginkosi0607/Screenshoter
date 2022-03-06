import os
import mss
from optparse import OptionParser

parser = OptionParser()
parser.add_option("-o", "--output", type="str", dest="d", help="The output file.")

(options, args) = parser.parse_args()
p = eval(options.__str__())
inp = p["d"].__str__()

if inp != "None":
        if os.path.isfile("./" + inp + ".png"):
                inpo = input("The file already exists do you want to wverite it? (y/n): ")
                if inpo == "n":
                        quit()
        with mss.mss() as sct:
                sct.shot(output="./" + inp + ".png")
else:
        num = 1
        while os.path.isfile("./" + 'scr' + str(num) + ".png"):
                num += 1
        with mss.mss() as sct:
                sct.shot(output="./" + "scr" + str(num) + ".png")