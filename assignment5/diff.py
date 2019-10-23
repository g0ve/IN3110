import sys
import glob

def main(input_file, output_file):

    with open(input_file, 'r') as iFile:
        ogVersion = iFile.read()
    with open(output_file, 'r') as oFile:
        modVersion = oFile.read()



if __name__ == '__main__':
    if len(sys.argv) == 3:
        lstFiles = glob.glob(sys.argv[1])
        lstFiles.append(glob.glob(sys.argv[2]))
    if all(lstFiles):
        print("Found all files :)\n")
        main(sys.argv[1], sys.argv[2])
    else:
        print("Cant find file/image. Make sure file/image is in your directory")
