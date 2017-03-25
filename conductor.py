import sys
from trackParser import writeToFile
from composer import compose

def init():
    action = sys.argv[1]

    if action == "grabData":
        sourceFolder = sys.argv[2]
        destinationFile = sys.argv[3]
        sequenceLength = sys.argv[4]
        writeToFile( sourceFolder, destinationFile, sequenceLength )

    elif action == "compose":
        # conductor.py source.json example.mid 240
        sourceFile = sys.argv[2]
        outputFileName = sys.argv[3]

        if len(sys.argv) > 4:
            length = sys.argv[4]
        else:
            length = 120

        compose(sourceFile, outputFileName, length)


init()
