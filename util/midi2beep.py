# based on https://github.com/dandroid88/midi-to-beep
import argparse, csv, os

parser = argparse.ArgumentParser(description='Convert midi files to beep tunes')
parser.add_argument('-f', type=str, help='a filepath to the midi you want played')
args = parser.parse_args()
tempo = 120
tempoMultiplier = 2


def getDuration(row, noteStart):
    return str((int(row[1].strip()) - noteStart)* tempoMultiplier)

def getFreq(row):
    return midiNumToFreq(int(row[4].strip()))

def midiNumToFreq(midiNumber):
    return 440 * pow(2, (midiNumber-69)/float(12))

def buildBeep():
    csvFile = csv.reader(open(args.f, 'r'))
    beepOut = ""
    noteStart = 0
    arrItems = 0
    for row in csvFile:
        if 'Note_on_c' in row[2]:
            if 0 == int(row[5].strip()):
                beepOut +=  "%.0f" % getFreq(row) + ', ' + getDuration(row, noteStart) + ', 0, '
                arrItems += 3
            else:
                noteStart = int(row[1].strip())
                outputFile = open(args.f.replace('.mid.csv', '.TcGVL'), 'w')
        elif 'Tempo' in row[2]:
            tempo = int(row[3].strip())

    beepOut += '0, 0, 0];\n\
END_VAR]]></Declaration>\n\
  </GVL>\n\
</TcPlcObject>'

    header = '<?xml version="1.0" encoding="utf-8"?>\n\
<TcPlcObject>\n\
  <GVL Name="' + os.path.basename(args.f).replace('.mid.csv', '') + '">\n\
    <Declaration><![CDATA[{attribute \'qualified_only\'}\n\
VAR_GLOBAL CONSTANT\n\
	BEEPS_MAX : UINT :=  ' + str(arrItems + 3) + ';	\n\
	Beeps : ARRAY[0..BEEPS_MAX] OF REAL := ['

    outputFile.write(header)
    outputFile.write(beepOut)
    return

if not args.f:
    parser.print_help()
else:
    buildBeep()
