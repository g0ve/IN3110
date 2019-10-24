import sys
import glob
import itertools


def main(input_file, output_file):

    with open(input_file, 'r') as iFile:
        ogVersion = iFile.read().split('\n')
    with open(output_file, 'r') as oFile:
        modVersion = oFile.read().split('\n')

    ogLineSet = set(ogVersion)
    modLineSet = set(modVersion)

    ogAdded = ogLineSet - modLineSet
    ogRemoved = modLineSet - ogLineSet
    similarities = modLineSet & ogLineSet

    ogLenght = len(ogVersion)
    modLenght = len(modVersion)
    lenght = 0
    i = 0

    if ogLenght > modLenght:
        lenght = ogLenght
    else:
        lenght = modLenght

    while i < lenght:

        if i < ogLenght:
            if ogVersion[i] in similarities:
                print('0 ' + ogVersion[i])
            if ogVersion[i] in ogAdded:
                print('- ' + ogVersion[i].strip())
            elif ogVersion[i] in ogRemoved:
                print('+ ' + ogVersion[i].strip())
        if i < modLenght:
            if modVersion[i] in ogAdded:
                print('- ' + modVersion[i].strip())
            elif modVersion[i] in ogRemoved:
                print('+ ' + modVersion[i].strip())

        i += 1

if __name__ == '__main__':
    if len(sys.argv) == 3:
        lstFiles = glob.glob(sys.argv[1])
        lstFiles.append(glob.glob(sys.argv[2]))
    if all(lstFiles):
        print("Found all files :)\n")
        main(sys.argv[1], sys.argv[2])
    else:
        print("Cant find file/image. Make sure file/image is in your directory")
