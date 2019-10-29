import sys
import argparse
import re
import glob
import highlighter

def main(syntax_file, input_file, flag):
    """
    This function goes throught a input text file line by line. It also goes throught
    a file with regex expressions. And if a word in a line match one of the expressions
    the line will be printed.

    But if a  flag (--highlighter) is given then highlight the matched word and print line.

    Paramters:
        syntax_file - File containing all regex expressions
        input_file - Text file where we find a match
        flag - A flag, if --highlight is true or not

    Return:
        None
    """
    lstSyntax = highlighter.open_syntax(syntax_file)
    i = 0
    rainbow = [91, 93, 92, 94, 95]
    with open(input_file, 'r') as iFile:
        for line in iFile:
            for syntax in lstSyntax:
                matches = re.findall(syntax[0],line)
                if(matches):
                    if(flag):
                        colored_line = highlighter.color_text(syntax, rainbow[i], line)

                        if(i < len(rainbow)-1):
                            i += 1
                        else:
                            i = 0
                        print(colored_line)
                    else:
                        print(line)


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
