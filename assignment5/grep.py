import sys
import argparse
import re
import glob
import highlighter

def main(syntax_file, input_file, flag):
    lstSyntax = highlighter.open_syntax(syntax_file)

    with open(input_file, 'r') as iFile:
        for line in iFile:
            for syntax in lstSyntax:
                matches=re.findall(syntax[0],line)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='UNIX utility knockkoff')

    parser.add_argument("syntax", type=str, help="Syntax file with all regex expr")
    parser.add_argument("input", type=str, help="Input filename with all lines to match")
    parser.add_argument("--highlight", help="A flag. Colors all the matched lines", action='store_true')

    args = parser.parse_args()

    lstFiles = glob.glob(args.syntax)
    lstFiles.append(glob.glob(args.input))

    if all(lstFiles):
        print("Found all files :)\n")
        main(args.syntax, args.input, args.highlight)
    else:
        print("Cant find file/image. Make sure file/image is in your directory")
