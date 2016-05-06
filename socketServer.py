import socket
import sys
from thread import *
 
HOST = ''   # Symbolic name meaning all available interfaces
PORT = 5469 # Arbitrary non-privileged port
 
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print 'Socket created'
 
#Bind socket to local host and port
try:
    s.bind((HOST, PORT))
except socket.error as msg:
    print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
    sys.exit()
     
print 'Socket bind complete'
 
#Start listening on socket
s.listen(10)
print 'Socket now listening'
 
#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome home\n') #send only takes string
    
	
    #infinite loop so that function do not terminate and thread do not end.
    while True:
         
        #Receiving from client
        data = "ID + Password:" + conn.recv(1024)# recieve id and password
		
		f = open("id.txt", 'r') # open id to read the current ID's
		f2 = open('temp.txt', 'w') # create our temp file
		
		for line in f:
			if line == conn.recv[0]:
				reply = 'Bad ID'
				
			else 
				reply = 'OK' 
				f2.write(data) 
				
				f2.close()
				f.close()
			
				f = open("id.txt", 'ab')
				f2 = open('temp.txt', 'r')
				
				for line in f2
					f.write("\n", line)
				f2.close()
				f.close() 
				os.remove("temp.txt")
					
        if not data: 
            break
			
        conn.sendall(reply)
     
    #came out of loop
    conn.close()
 
#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print 'Connected with ' + addr[0] + ':' + str(addr[1])
     
    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))
 
s.close()