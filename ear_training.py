import midi
import random
from datetime import datetime
import os

def playA4 ():
	onA4 = midi.NoteOnEvent (tick = 0, data = [57, 100])	
	offA4 = midi.NoteOffEvent (tick = 500, data = [57, 100])	
	track.append (onA4)
	track.append (offA4)

def play_pitch (pitch):
	onT = midi.NoteOnEvent (tick = 0, data = [pitch, 100])	
	offT = midi.NoteOffEvent (tick = 200, data = [pitch, 100])	
	track.append (onT)
	track.append (offT)

def check_chord (pitch, maj):

	if pitch == 45 or pitch == 57:
		strpitch = 'A'
	if pitch == 46 or pitch == 58:
		strpitch = 'A# || Bb'
	if pitch == 47 or pitch == 59:
		strpitch = 'B || Cb'
	if pitch == 48:
		strpitch = 'C'
	if pitch == 49:
		strpitch = 'C# || Db'
	if pitch == 50:
		strpitch = 'D'
	if pitch == 51:
		strpitch = 'D# || Eb'
	if pitch == 52:
		strpitch = 'E || Fb'
	if pitch == 53:
		strpitch = 'F'
	if pitch == 54:
		strpitch = 'F# || Gb'
	if pitch == 55:
		strpitch = 'G'
	if pitch == 56:
		strpitch = 'G# || Ab'

	check = 0
	while check == 0:
		chord = raw_input ('\nWhat was the chord?\n')

		T = 0
		if chord [0] == 'A' or chord [0] == 'a':
			T = 45
		elif chord [0] == 'B' or chord [0] == 'b':
			T = 47
		elif chord [0] == 'C' or chord [0] == 'c':
			T = 48
		elif chord [0] == 'D' or chord [0] == 'd':
			T = 50
		elif chord [0] == 'E' or chord [0] == 'e':
			T = 52
		elif chord [0] == 'F' or chord [0] == 'f':
			T = 53
		elif chord [0] == 'G' or chord [0] == 'g':
			T = 55
		else:
			check = 0
			print 'ERROR!!! Check the input again'
			continue

		if chord [1] == '#':
			T = T + 1
		elif chord [1] == 'b':
			T = T - 1

		if pitch == T or pitch == T+12:
			print '\t\t\t\tRIGHT pitch\n'
		else:
			print '\t\t\t\tWRONG pitch\n\t\t\t\t\tIt was ' + strpitch + '\n'

		if 'maj' in chord or 'Maj' in chord or 'MAJ' in chord:
			check = 1
			if maj == 1:
				print '\t\t\t\tRIGHT tone\n' 
			else:
				print '\t\t\t\tWRONG tone\n\t\t\t\t\tIt was MIN\n'
		elif 'min' in chord or 'Min' in chord or 'MIN' in chord:
			check = 1
			if maj == 0:
				print '\t\t\t\tRIGHT tone\n' 
			else:
				print '\t\t\t\tWRONG tone\n\t\t\t\t\tIt was MAJ\n'
		else:
			check = 0
			print 'ERROR!!! Check the input again'
		

keep_working = 'Y'
while keep_working == 'y' or keep_working == 'Y' or keep_working == 'yes' or keep_working == 'YES':

	random.seed (datetime.now ())

	pattern = midi.Pattern ()
	track = midi.Track ()
	pattern.append (track)

	playA4 ()

	pitch = random.randint (45, 59)

	maj = random.randint (0,1)
	if maj == 1:
		play_pitch (pitch)
		play_pitch (pitch+4)
		play_pitch (pitch+7)
		play_pitch (pitch+12)
	else:
		play_pitch (pitch)
		play_pitch (pitch+3)
		play_pitch (pitch+7)
		play_pitch (pitch+12)


	eot = midi.EndOfTrackEvent (tick = 1)
	track.append (eot)

	fname = 'tmp_track.mid'
	midi.write_midifile (fname, pattern)

	os.system ('timidity ' + fname)
	os.system ('rm -f ' + fname)
	
	check_chord (pitch, maj)

	keep_working = raw_input ('Do you want to keep training? [Y/n] \n')
	if keep_working == '':
		keep_working = 'Y'
