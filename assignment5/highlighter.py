import glob
import re
import sys

def main(syntax_file, theme_file, output_file):
    input_file = "hello.ny"
    regexTheme = r"(.*): (\d*;\d*)"
    lstTheme = []
    dictTheme = {}
    regexSyntax = r'"(.*)": (.*)'
    lstSyntax = []

    with open(syntax_file, 'r') as sFile:
        txtSyntax = sFile.read()
        lstSyntax = re.findall(regexSyntax, txtSyntax)

    with open(theme_file, 'r') as tFile:
        txtTheme = tFile.read()
        lstTheme = re.findall(regexTheme, txtTheme)

        for (name, color_sequence) in lstTheme:
            dictTheme[name] = color_sequence


    with open(input_file, 'r') as iFile:
        txtInput = iFile.read()
    with open(output_file, 'w') as oFile:
        for syntax in lstSyntax:
            regex = "(" + syntax[0] + ")"
            name = syntax[1]
            color_sequence = dictTheme[name]
            start_code = "\033[{}m".format(color_sequence)
            end_code = "\033[0m"

            txtColored = re.sub(regex, start_code + r"\1" + end_code, txtInput)
            print(txtColored)

            oFile.write(txtColored)


            print("\nText has been colored o/" )










if len(sys.argv) == 4:
    lstFiles = glob.glob(sys.argv[1])
    lstFiles.append(glob.glob(sys.argv[2]))
    lstFiles.append(glob.glob(sys.argv[3]))
if all(lstFiles):
    print("Found all files :)\n")
    main(sys.argv[1], sys.argv[2], sys.argv[3])
else:
    print("Cant find file/image. Make sure file/image is in your directory")
