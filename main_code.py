#!/usr/bin/python3 -tt
# Credit Pycon 2016
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Regular expressions
# Fill in the code for the functions below. main() is already set up
# to call the functions with a few different inputs,
# printing 'OK' when each function is correct.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code.
# Please do not edit anything within 
# #### BEGIN DO NOT EDIT and
# #### END DO NOT EDIT lines


# A. has_vowel
# Check if the string passed to function has a vowel, if so return True,
# otherwise return false. Recall the following syntax:
# bool(re.search(r'hello', sentence)) 
import re 

def has_vowel(s):
  # +++your code here+++
  test = bool(re.search(r'[a,e,i,o,u]', s))
  return test


# B. is_integer
# Given a string s, return True iff the string represents a 
# valid integer.
def is_integer(s):
  # +++your code here+++
  test = bool(re.match(r"[-]?\d+$", s))
  return test


# C. is_fraction
# Given a string s, return True iff the string represents
# a valid fraction
def is_fraction(s):
  # +++your code here+++
  test = bool(re.match(r"\s*(\d[-]+|[/-])", s))
  return test


# D. get_extension
#Return the file extension for a full file path.
def get_extension(s):
  # +++your code here+++
  test=re.split(r"\.\s*", s)
  return test[1]

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

  print('is_vowel')
  # Each line calls cupcakes, compares its result to the expected for that call.
  score+= test(has_vowel("rhythm"), False)
  score+= test(has_vowel("exit"), True)
  score+= test(has_vowel("no"), True)
  score+= test(has_vowel("yes"), True)
  score+= test(has_vowel("%^&"), False)

  print('is_integer')
  score+= test(is_integer("5"), True)
  score+= test(is_integer("a5"), False)
  score+= test(is_integer("-199"), True)
  score+= test(is_integer("+999"), False)
  score+= test(is_integer("0"), True)

  print('is_fraction')
  score+= test(is_fraction("-999/1"), True)
  score+= test(is_fraction("5000"), False)
  score+= test(is_fraction("0/5"), True)
  score+= test(is_fraction("+999/1"), False)
  score+= test(is_fraction("5/"), False)
  
  print('get_extension')
  score+= test(get_extension("hello.zip"), "zip")
  score+= test(get_extension("test.py"), "py")
  score+= test(get_extension("bad_document.docx"), "docx")
  score+= test(get_extension("good_document.tex"), "tex")
  score+= test(get_extension("hello_world_1.py"), "py")

  print('Your current score is: {}'.format(score))

  f_temp = open("temp_grade", "w+")
  f_temp.write(str(score))

# Standard boilerplate to call the main() function.
if __name__ == '__main__':
  main()
#### END DO NOT EDIT
