import midi
import os
import sys
import random
from Markov import Markov

NOTE_VELOCITY = 50
NOTE_DURATION = [110, 220, 440]

def get_rand_duration():
    """
    This just randomly picks between eigth, quarter, and whole notes to add some
    variety
    """
    prob = random.randint(0, 100)
    if prob < 60:
        return 1
    elif prob < 90:
        return 2
    else:
        return 0

def compose(sourceFile, outputFileName, length):
    markov = Markov(sourceFile)

    sequenceLength = markov.sequenceLength()

    # Build random beging of song
    notes = []
    for i in range(sequenceLength):
        notes.append( random.randint(50,60) )

    # Build list of notes
    while( len(notes) < length):
        newNote = markov.get( notes[-sequenceLength:] )
        if newNote is not None:
            notes.append(int(newNote))
        else:
            print "INFO: No possible note found"
            del notes[-1]

    print "Song Composed:"
    print notes

    # Make patern into
    pattern = midi.Pattern()
    pattern.make_ticks_abs()
    track = midi.Track()
    pattern.append(track)

    for note in notes:
        on = midi.NoteOnEvent(tick=0, velocity=NOTE_VELOCITY, pitch=note)
        off = midi.NoteOffEvent(tick=NOTE_DURATION[get_rand_duration()], pitch=note)
        track.append(on)
        track.append(off)

    eot = midi.EndOfTrackEvent(tick=1)
    track.append(eot)
    midi.write_midifile(outputFileName, pattern)

    print "Song written to file: %s" % outputFileName
