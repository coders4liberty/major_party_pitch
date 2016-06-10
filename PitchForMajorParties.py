def pitch(iSupport, iOppose, ThirdPartyCandidates, heOrShe):
	for peep in ThirdPartyCandidates:
		print "It does not matter that", peep, "is not", iOppose, "\b."
	print "What matters is that", iSupport, "is not", iOppose, "\b!"
	print"Therefore you must support", iSupport, "\b!"
	print heOrShe, "is the only one that is not", iOppose, "that can win"
	print "(because people like me support", iSupport, "\b)!"
	print "It does not matter how", iSupport, "stands on the issues."
	print "Let's jump off this cliff together!"
	print "Who cares what your mom told you when you were a kid!"
	print "That does not matter now!"
	print "We cannot allow", iOppose, "to win!"

ThirdPartyCandidates = ['Gary Johnson', 'Jill Stein']

pitch('Hillary', 'Trump', ThirdPartyCandidates, 'She')
print("\n")
pitch('Trump', 'Hillary', ThirdPartyCandidates, 'He')
