import glob
import re
import sys
def color_text(syntax, dictTheme, txtSource):
    """
    This function take a syntax, dict of themes or theme code and colors matched
    group 1 in regex with correct color from theme in the source file given.

    Paramters:
        syntax - A regex expressions + name
        dictTheme - This is either a dict with themes or just a color sequence
        txtSource - source text you want to color

    Return:
        txtSource - this is the source file colored
    """
    regex = syntax[0]
    name = syntax[1]
    if(type(dictTheme) is int):
        color_sequence = dictTheme
    else:
        color_sequence = dictTheme[name]

    start_code = "\033[{}m".format(color_sequence)
    end_code = "\033[0m"
    finish_code = start_code + r"\1" + end_code
    txtSource = re.sub(regex, finish_code, txtSource)

    return txtSource

def open_syntax(filename):
    """
    This function opens a file containing syntax. After opening the file it finds
    all syntax in that file with a regex expression and puts it all in a list

    Paramters:
        filename - filename containing syntax

    Return:
        lstSyntax - returns the list with all syntax in given file
    """
    regexSyntax = r'"(.*)": (.*)'
    with open(filename, 'r') as sFile:
        txtSyntax = sFile.read()
        lstSyntax = re.findall(regexSyntax, txtSyntax)
    return lstSyntax

def main(syntax_file, theme_file, sourcefile_to_color):
    """
    This function opens a file containing themes, and opens the source file you want to color.
    After that it finds all themes in the theme file and puts it in a dict.
    When that is done it calls the color_text function.
    and prints out the colored file + a message to user.

    Paramters:
        syntax_file - File containing all regex expressions
        theme_file - File containing all themes
        sourcefile_to_color - source file you want to color

    Return:
        None
    """
    regexTheme = r"(.*): (\d*;\d*)"
    lstTheme = []
    dictTheme = {}
    lstSyntax = open_syntax(syntax_file)


    with open(theme_file, 'r') as tFile:
        txtTheme = tFile.read()
        lstTheme = re.findall(regexTheme, txtTheme)

        for (name, color_sequence) in lstTheme:
            dictTheme[name] = color_sequence


    with open(sourcefile_to_color, 'r') as srcFile:
        txtSource = srcFile.read()
        for syntax in lstSyntax:
            txtSource = color_text(syntax, dictTheme, txtSource)
        print(txtSource)
        print("\nText has been colored o/" )

if __name__ == '__main__':
    if len(sys.argv) == 4:
        lstFiles = glob.glob(sys.argv[1])
        lstFiles.append(glob.glob(sys.argv[2]))
        lstFiles.append(glob.glob(sys.argv[3]))
    if all(lstFiles):
        print("Found all files :)\n")
        main(sys.argv[1], sys.argv[2], sys.argv[3])
    else:
        print("Cant find file/image. Make sure file/image is in your directory")

