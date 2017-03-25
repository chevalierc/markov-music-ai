import midi
import os
import sys
import random
from Markov import Markov

def writeToFile(sourcefolderName, outputFileName, sequenceLength):
    markov = Markov()
    folderName = os.path.abspath(sourcefolderName)
    files = getFiles(folderName)
    print str(len(files)) + " files found"

    #parse each file and push to markovDS
    for fileName in files:
        parseFile(fileName, markov, sequenceLength)

    print "Files parsed"

    #write as json to file
    markov.writeToFile(outputFileName)
    print "Markov written to file"

def parseFile(midi_file, markov, sequenceLength):
    """
    parse each file and add data to markob object
    """
    tracks = midi.read_midifile(midi_file)
    sequenceLength = int(sequenceLength)

    # Get each track
    while True:
        if len(tracks):
            individual_track = tracks.pop()

            #Get each note in the track
            previousNotes = []
            for event in individual_track:
                if type(event) is midi.NoteOnEvent:
                    note = event.data[0]
                    if len(previousNotes) >= sequenceLength:
                        markov.push( previousNotes[-sequenceLength:] , note)
                    previousNotes.append(note)

        else:
            break


def getFiles(folderName):
    """
    Look in each folder of the current directory for files ending in .mid
    """
    allFiles = []
    files = os.listdir( folderName )
    for item in files:
        item = os.path.join(folderName, item)
        if os.path.isdir(item):
            allFiles += getFiles( item )
        else:
            if item.endswith('.mid'):
                allFiles.append(item)

    return allFiles

if __name__ == '__main__':
    folderName= sys.argv[1]
    print "Parsing %s" % folderName
    folders(folderName)
    i = 0;
    for num in range(0,10000):
        if markov.get( (46,64) ) == 67:
            i += 1
