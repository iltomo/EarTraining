# EarTraining
Ear Training softwarfe in python

This software allows to listen to Maj and Min chords on piano, using A4 as reference pitch. Then it ask you what chord it is. The answer must be in the form pitch-modification-tone, i.e. if the chord is BbMaj, the answer must be written as:

BbMaj

If there isn't any modification, the tone must follow the pitch, i.e. for GMin, the answer must be written as:

Gmin

The code isn't case sensitive except for the modification b that must be written lowercase.

# Requirements

This code use the python-midi module in order to work with midi: 
https://github.com/vishnubob/python-midi

To play the midi, Timidity is used.
