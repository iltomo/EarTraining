import midi
import random
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
	check = 0
	while check == 0:
		chord = raw_input ('What was the chord?\n')

		T = 0
		if chord [0] == 'A' or chord [0] == 'a':
			T = 57
		elif chord [0] == 'B' or chord [0] == 'b':
			T = 59
		elif chord [0] == 'C' or chord [0] == 'c':
			T = 60
		elif chord [0] == 'D' or chord [0] == 'd':
			T = 62
		elif chord [0] == 'E' or chord [0] == 'e':
			T = 64
		elif chord [0] == 'F' or chord [0] == 'f':
			T = 65
		elif chord [0] == 'G' or chord [0] == 'g':
			T = 67
		else:
			check = 0
			print 'ERROR!!! Check the input again'
			continue

		if chord [1] == '#':
			T = T + 1
		elif chord [1] == 'b':
			T = T - 1

		if pitch == 69 and T == 57:
			print '\t\t\t\tRIGHT pitch\n'
		elif pitch == T:
			print '\t\t\t\tRIGHT pitch\n'
		else:
			print '\t\t\t\tWRONG pitch\n'

		if 'maj' in chord or 'Maj' in chord or 'MAJ' in chord:
			check = 1
			if maj == 1:
				print '\t\t\t\tRIGHT tone\n' 
			else:
				print '\t\t\t\tWRONG tone\n'
		elif 'min' in chord or 'Min' in chord or 'MIN' in chord:
			check = 1
			if maj == 0:
				print '\t\t\t\tRIGHT tone\n' 
			else:
				print '\t\t\t\tWRONG tone\n'
		else:
			check = 0
			print 'ERROR!!! Check the input again'
		

SEED = input ('Give me a number\n')
n = 0
keep_working = 'Y'
while keep_working == 'y' or keep_working == 'Y' or keep_working == 'yes' or keep_working == 'YES':

	n = n+1
	random.seed (SEED+n)

	pattern = midi.Pattern ()
	track = midi.Track ()
	pattern.append (track)

	playA4 ()

	pitch = random.randint (57, 69)

	play_pitch (pitch)

	maj = random.randint (0,1)
	if maj == 1:
		play_pitch (pitch+4)
		play_pitch (pitch+7)
		play_pitch (pitch+12)
		play_pitch (pitch+7)
		play_pitch (pitch+4)
	else:
		play_pitch (pitch+3)
		play_pitch (pitch+7)
		play_pitch (pitch+12)
		play_pitch (pitch+7)
		play_pitch (pitch+3)

	play_pitch (pitch)

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
