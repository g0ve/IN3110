import argparse
from blur_1 import main as blur_1
from blur_2 import main as blur_2
from blur_3 import main as blur_3

parser = argparse.ArgumentParser(description='Blur image program')

parser.add_argument("-pp","--purePython", help="Blurs an image with pure python code", action='store_true')
parser.add_argument("-np","--numpy", help="Blurs an image with with help of Numpy", action='store_true')
parser.add_argument("-nb","--numba", help="Blurs an image with help of Numba", action='store_true')
parser.add_argument("-i","--input", help="If you want to specify a input file :)", default='beatles.jpg')
parser.add_argument("-o","--output", help="If you want to specify a output file :)", default='blurred_image.jpg')

args = parser.parse_args()

if args.purePython:
    blur_1(args.input, args.output)

elif args.numpy:
    blur_2(args.input, args.output)

elif args.numba:
    blur_3(args.input, args.output)

else:
    print("This didnt quit work. Try: $python blur.py --help")