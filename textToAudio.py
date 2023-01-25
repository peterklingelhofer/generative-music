from midiutil import MIDIFile
import string
from tqdm import tqdm


def generateScaleNotes(root, scale_type):
    if scale_type == 'major':
        intervals = [2, 2, 1, 2, 2, 2, 1]
    elif scale_type == 'minor':
        intervals = [2, 1, 2, 2, 1, 2, 2]
    else:
        raise ValueError(f'Invalid scale type: {scale_type}')
    notes = [root]
    for interval in intervals:
        notes.append(notes[-1] + interval)
    return notes


def textToMidi(text, file_name, key='C', scale_type='major'):
    mf = MIDIFile(1)
    track = 0
    time = 0

    mf.addTrackName(track, time, "Text to MIDI")
    mf.addTempo(track, time, 100)

    text = text.upper().translate(str.maketrans('', '', string.punctuation))

    midiNoteValues = {'A': 60, 'B': 62, 'C': 64, 'D': 65, 'E': 67, 'F': 69,
                      'G': 71, 'H': 72, 'I': 74, 'J': 75, 'K': 77, 'L': 79,
                      'M': 81, 'N': 83, 'O': 84, 'P': 86, 'Q': 88, 'R': 90,
                      'S': 92, 'T': 93, 'U': 95, 'V': 97, 'W': 98, 'X': 100,
                      'Y': 102, 'Z': 104}

    root_note = ord(key.upper()) - ord('A') + 60
    notes = generateScaleNotes(root_note, scale_type)

    for letter in tqdm(text):
        if letter in midiNoteValues:
            pitch = min(notes, key=lambda x: abs(x - midiNoteValues[letter]))
            channel = 0
            duration = 0.5
            volume = 100
            mf.addNote(track, channel, pitch, time, duration, volume)
            time += duration

    with open(file_name, 'wb') as outf:
        mf.writeFile(outf)


textToMidi("This is your text to be converted to music",
           "output.mid", key='C', scale_type='minor')


def testTextToMidi():
    textToMidi("This is a test of the text to MIDI conversion",
               "output.mid", key='C', scale_type='major')
    textToMidi("This is a test of the text to MIDI conversion",
               "output.mid", key='G', scale_type='minor')
    textToMidi("This is a test of the text to MIDI conversion",
               "output.mid", key='A', scale_type='minor')


testTextToMidi()
