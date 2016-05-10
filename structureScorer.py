import words.py
import os
import hashlib

BLOCKSIZE = 65536

hasher = hashlib.md5()

adjectiveList1 = open('adjectives.txt', 'rb')
master = open('masterRecord.txt', 'wb')

adjective = 1
noun = 2
verb = 3
adverb = 4
pronoun = 5

adjective2 = 0
noun2 = 0
verb2 = 0
adverb2 = 0
pronoun2 = 0

adjectivesList = []

### ANALYZE TEMPSTRUC FILES HERE ###


for filename in os.listdir("C:\Users\Matt\Desktop\AI project"): # where I'm storing everything 
	if filename.startswith("tempStruc"): # if our file starts with tempstruc 
		struc = open(filename, 'rb') # open the file if it begins with what we're looking for
		temp = opem("temp.txt", 'wb')
		
		for line in struc:
			if line == "adjective": # if it's an adjective 
				temp.append(adjective)
			if line == "noun": 
				temp.append(noun)
			if line == "verb": 
				temp.append(verb)
			if line == "adverb":
				temp.append(adverb)
			if line == "pronoun":
				temp.append(pronoun)
		
		temp.close()
				
		with open('temp.txt', 'rb') as afile:
			buf = afile.read(BLOCKSIZE)
			while len(buf) > 0:
				hasher.update(buf)
				buf = afile.read(BLOCKSIZE)
				
		tempVar = 0
		hash = hasher.hexdigest() + "\n" 
		
		for line in master:
			if line == hash: # if our hash is already in the file 
				tempVar++
				
			else master.write(hash) # make our hash variable with a new line at the end and write it to file 
			
		for line in counter:
			# need to write our counter to it so as to keep track of structure scoring