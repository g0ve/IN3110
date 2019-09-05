#!/usr/bin/env python
import sys
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
    file = open(filename, "r") #Opens the file we are going to read from

    a = 0
    b = 0
    c = 0

    with open(filename) as f:
        for line in f:
            a += 1
            c += len(line)
            for words in line.split():
                b += 1

    print("File {} has:\n\t{} lines\n\t{} words\n\t{} characters".format(filename, a, b, c))

fileCounter("poem.txt")
