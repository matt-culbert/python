import os

master = open('masterRecord.txt', 'wb')
temp = []

adjective = 1
noun = 2
verb = 3
adverb = 4
pronoun = 5

### ANALYZE TEMPSTRUC FILES HERE ###

for filename in os.listdir("C:\Users\Matt\Desktop\AI project"): # where I'm storing everything 
	if filename.startswith("tempStruc"): # if our file starts with tempstruc 
		struc = filename
		
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
		
		for line in master:
			if line = temp: # if our struc already in master
				sum = line.split(' ',1)[1]# now split the line and everything after our first algorithm is the number we need
				sum = sum + 1
				final = temp + sum
				line.write(final) # write the struc + it's count +1 to the master
			
			else here = temp + " 1" master.append(here) # if it's not there write it with it's first count
			
struc.close()
master.close()