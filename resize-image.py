#!/usr/bin/env python

import getopt
import sys
from os import path

dirpath = path.join(path.dirname(__file__), 'pylib')
if dirpath not in sys.path:
    sys.path.append(dirpath)

from shell_utils import Format

try:
    from PIL import Image
except Exception as e:
    print (Format.red('\tFirst you need to install Pillow'))
    print('\t\tUse \'%s\' to install it' % Format.cyan('sudo pip install pil'))
    sys.exit(0)


def usage():
    print ('  %5s %s %s' % ('-i', '--input [file]'.ljust(18), 'path to file to be resized'))
    print ('  %5s %s %s' % ('-o', '--output [file]'.ljust(18), 'path to the generated file (optional)'))
    print ('  %5s %s %s' % ('-w', '--width [size]'.ljust(18), 'desired width of generated file'))


try:
    opts, args = getopt.getopt(sys.argv[1:], "i:o:w:", [
                               "width", "output", "input"])
except getopt.GetoptError as err:
    print str(err)
    usage()
    sys.exit(2)

outputFile = None
inputFile = None
width = None

for o, a in opts:
    if o in ('-i', '--input'):
        inputFile = a
    elif o in ("-o", "--output"):
        outputFile = a
    elif o in ("-w", "--width"):
        width = int(a)
    else:
        assert False, "unhandled option"

if not inputFile or not width:
    usage()
    sys.exit(2)

if not outputFile:
    outputFile = inputFile

print ("Resizing %s to width %s" % (inputFile, width))
img = Image.open(path.realpath(inputFile))
wpercent = (width / float(img.size[0]))
hsize = int((float(img.size[1]) * float(wpercent)))
img = img.resize((width, hsize), Image.ANTIALIAS)
img.save(path.realpath(outputFile))

print (Format.green("Image generated %s" % outputFile))
