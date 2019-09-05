#!/usr/bin/env python
import sys
import glob
"""

In this fucntion we find a, b, and c in a given file.
a - number of lines in a file
b - number of words
c -number of characters

To find 'a' we use a simple for loop to add 1 to a counter for every line in file.
To find 'b' we use the cheatsheet and sees that we can use line.split()
To find 'c' we again use the cheatsheet and sees we can use len() function.

"""

def fileCounter(filename):
    a = 0
    b = 0
    c = 0

    with open(filename) as f:
        for line in f:
            a += 1
            c += len(line)
            for words in line.split():
                b += 1

    print("File {} has:\n\t{} lines\n\t{} words\n\t{} characters\n".format(filename, a, b, c))

"""
So the scipt can be called with 'wc *' or 'wc *.py'. I found that i can use the module glob.
This returs a list of all files, which I can go trought with a loop.
"""
if len(sys.argv) == 2:
    lstFiles = glob.glob(sys.argv[1])
    if len(lstFiles) == 0:
        print("Cant find file. Try '*' for all files in directory")
    else:
        for file in lstFiles:
            fileCounter(file)
else:
    print("This script needs a filename has parameter. Or '*' for all files in directory")
