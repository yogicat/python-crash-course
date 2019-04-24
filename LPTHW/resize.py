from sys import argv
from PIL import Image

if len(argv) != 4:
    exit("python resize.py n infile outfile")

n = int(argv[1])
infile = argv[2]
outfile = argv[3]
