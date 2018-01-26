#!/usr/bin/python -tt
# Credit Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0
# Basic string exercises
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# Please do not edit anything within
# #### BEGIN DO NOT EDIT and
# #### END DO NOT EDIT lines
# A. cupcakes
# Given an int count of a number of cupcakes, return a string
# of the form 'Number of cupcakes: <count>', where <count> is the number
# passed in. However, if the count is 25 or more, then use the word 'too many'
# instead of the actual count.
# So cupcakes(5) returns 'Number of cupcakes: 5'
# and cupcakes(23) returns 'Number of cupcakes: too many'
def cupcakes(count):
	# +++your code here+++
	error = 'Number of cupcakes: too many'
	if count < 25:
		numOfCupcakes = "Number of cupcakes: " + str(count)
		return numOfCupcakes
	else: return error

# B. string_ends
# Given a string s, return a string made of the first 3
# and the last 3 chars of the original string,
# so 'student' yields 'stuent'. However, if the string length
# is less than 3, return instead the empty string.
def string_ends(s):
	# +++your code here+++
	error = ''
	if len(s) < 3:
		return error
	else: 
		first = s[:3]
		last = s[-3:]
		full = first + last
		return full
# C. add_asterisks
# Given a string s, return a string
# where all occurrences of its first char have
# been changed to '*', except do not change
# the first char itself.
# e.g. 'babble' yields 'ba**le'
# Assume that the string is length 1 or more.
# Hint: s.replace(str_a, str_b) returns a version of string s
# where all instances of str_a have been replaced by str_b.
def add_asterisks(s):
	firstL = s[0]
	remainingL = s[1:]
	
	remainingL = remainingL.replace(firstL, '*') 

	s = firstL + remainingL
	
	return s
# D. Mix_concat
# Given strings a and b, return a single string with a and b separated
# by a space '<a> <b>', except swap the first 2 chars of each string.
# e.g.
#   'mix', 'pod' -> 'pox mid'
#   'dog', 'dinner' -> 'dig donner'
# Assume a and b are length 2 or more.
def mix_concat(a, b):
	# +++your code here+++
	firstL = a[0:2]
	remainingL = a[3:]
	secondL = b[0:2]
	remainingLb = b[3:]
	
	a = secondL + remainingL
	b = firstL + remainingLb
	
	return a, b

#### BEGIN DO NOT EDIT
# Provided simple test() function used in main() to # what each function returns vs. what it's supposed to return.
def test(got, expected, points = 1):
	if got == expected:
		prefix = ' OK '
	else:
		prefix = '  X '
		print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
		grade = 0
	if(prefix == ' OK '):
		grade = points
	return grade
# Provided main() calls the above functions with interesting inputs,
# using test() to check if each result is correct or not.
def main():
	score = 0
	print('cupcakes')
	# Each line calls cupcakes, compares its result to the expected for that call.
	score+= test(cupcakes(7), 'Number of cupcakes: 7')
	score+= test(cupcakes(10), 'Number of cupcakes: 10')
	score+= test(cupcakes(26), 'Number of cupcakes: too many')
	score+= test(cupcakes(99), 'Number of cupcakes: too many')
	print('string_ends')
	score+= test(string_ends('student'), 'stuent')
	score+= test(string_ends('Wednesday'), 'Wedday')
	score+= test(string_ends('b'), '')
	score+= test(string_ends('xyz'), 'xyzxyz')
	print('add_asterisks')
	score+= test(add_asterisks('babble'), 'ba**le')
	score+= test(add_asterisks('aardvark'), 'a*rdv*rk')
	score+= test(add_asterisks('google'), 'goo*le')
	score+= test(add_asterisks('donut'), 'donut')
	print('mix_concat')
	score+= test(mix_concat('mix', 'pod'), 'pox mid')
	score+= test(mix_concat('dog', 'dinner'), 'dig donner')
	score+= test(mix_concat('gnash', 'sport'), 'spash gnort')
	score+= test(mix_concat('pezzy', 'firm'), 'fizzy perm')
	print('Your current score is: {}'.format(score))
	f_temp = open("temp_grade", "w+")
	f_temp.write(str(score))
# Standard boilerplate to call the main() function.
if __name__ == '__main__':
	main()
#### END DO NOT EDIT