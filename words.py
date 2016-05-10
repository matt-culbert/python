### holds our functions for reading file data and structuring it ###
import random
import os
import glob 

# our class for all file related handling 
class FileHandle:

	def __init__(self, name):
		self.name = name 
		
		### INSTANCED VARS AND LISTS FOR LATER ###
		# we read our structures into these lists
		self.adjectivesList = [] 
		self.verbsList = []
		self.pronounsList = []
		self.adverbsList = []
		self.nounsList = []
		
		adjectiveList1 = open('adjectives.txt', 'rb')
		verbsList1 = open('verbs.txt', 'rb')
		pronounsList1 = open('pronouns.txt', 'rb')
		adverbsList1 = open('adverbs.txt', 'rb')
		nounsList1 = open('nouns.txt', 'rb')
		structure = open('structure.txt', 'wb')
		mapping = open('mapping.txt', 'wb')

		for line in adjectiveList1:
			adjectivesList.append(line) # for every adjective in our file, append it to our list 
			
		for line in verbsList1:
			verbsList.append(line) 
		
		for line in pronounsList1:
			pronounsList.append(line)
			
		for line in adverbsList1:
			adverbsList.append(line) 
			
		for line in nounsList1:
			nounsList.append(line)  
		
	def structureCount(tempSentence, nounsList, adverbsList, pronounsList, verbsList, adjectivesList): # this function simply counts the number of adverbs, adjectives, so on. Needs a sentence and the wordlists  
		# word count 
		nouns = 0
		verbs = 0
		adverbs = 0
		pronouns = 0
		adjectives = 0
		
		for line in tempSentence: #reads our temp sentence container
			if line = adjectivesList: # if our word is in our adjectives list 
				adjectives++ # add one to adjectives var 
				
				for line in structure: # find the adjectives line 
					if line = 'Adjective':
					line.append(' ', adjectives) # add our adjectives count to the end of it 
					
			else if line = verbsList:
				verbs++ # add one to verbs var 
				
				for line in structure: # find the verbs line 
					if line = 'Verb':
					line.append(' ', verbs) # add our verbs count to the end of it
			
			else if line = pronounsList:
				pronouns++ # add one to pronouns var 
				
				for line in structure: # find the pronouns line 
					if line = 'Pronoun':
					line.append(' ', pronouns) # add our pronouns count to the end of it
			
			else if line = adverbsList:
				adverbs++ # add one to adverbs var 
				
				for line in structure: # find the adverbs line 
					if line = 'Adverb':
					line.append(' ', adverbs) # add our adverbs count to the end of it
			
			else if line = nounsList:
				nouns++ # add one to noun var 
				
				for line in structure: # find the noun line 
					if line = 'Noun':
					line.append(' ', nouns) # add our nouns count to the end of it
					
			else print ('Bad word')
			
		wordlist.close()
		structure.close()
		mapping.close()

	def structureMapping(tempSentence): # this maps the structure to essentially noun verb adjective, basic replace function
		try: # try to make our new file THIS WONT CATCH US OPENING WRONG FILE 
			tempStruc = "tempStruc" + rand.int(1,100000000) + ".txt"
		except *:
			print ("Error encountered, trying again...")
			tempStruc = "tempStruc" + rand.int(1,100000000) + ".txt"
		
		temp = open(tempStruc, 'wb')
		adjectiveList1 = open('adjectives.txt', 'rb')
		
		for line in tempSentence:
			if line == adjectivesList:
				temp.write("Adjective") # write our new adjective to the file to get an idea of the sentence structure 
					
			else if line == verbsList:
				temp.write("Verb")
				
			else if line == adverbsList:
				temp.write("Adverb")
				
			else if line == pronounsList:
				temp.write("Pronoun")
			
			else if line == nounsList:
				temp.write("Noun")
			
			else print ("Word not in data base!")
			
		adjectiveList1.close()
		temp.close()
		
	def structureScore(file): # function to create our score of most common structures, assumes we've opened a file already and are passing its contents to this 
		for line in file:
			if line.startswith("Adjective:"):
				total = "Adjective: " + sum([int(num) for num in line]) 
				line.write(total) # write the new total to the line 

### MAIN BODY ###			
while 1:
	input = input("Type your sentence to analyze here: ")
	try:
		structureCount(input)
		structureMapping(input)
		structureScore(input)
	except *:
		print("Problem analyzing!")