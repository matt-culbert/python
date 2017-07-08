import socket
from struct import *
import datetime
import pcapy
import sys
import sqlite3 as lite
#from geoip import geolite2

global1 = lite.connect('global.db')
flagged1 = lite.connect('flagged.db')

#with global1:

#    cur = global1.cursor()
#    cur.execute("CREATE TABLE Current_Traffic(Source_Address TEXT, Destination_Address TEXT, Source_Mac TEXT, Destination_Mac TEXT, )")

global_dict={'source addresses': [''], 'destination addresses': [''], 'source mac': [''], 'destination mac': ['']} # empty dict to store new addresses in
flagged_dict={'Event': [''], 'Source Addresses': [''], 'Destination Addresses': ['']}

def geoip_search(IP):
    '''
    open device
    # Arguments here are:
    #   IP addr
    '''
    match = geolite2.lookup(IP)
    return match.country

def main(argv):
    #list all devices
    devices = pcapy.findalldevs()
    print devices

    #ask user to enter device name to sniff
    print "Available devices are :"
    for d in devices :
        print d

    dev = raw_input("Enter device name to sniff : ")

    print "Sniffing device " + dev

    '''
    open device
    # Arguments here are:
    #   device
    #   snaplen (maximum number of bytes to capture _per_packet_)
    #   promiscious mode (1 for true)
    #   timeout (in milliseconds)
    '''
    cap = pcapy.open_live(dev , 65536 , 1 , 0)

    #start sniffing packets
    while(1) :
        (header, packet) = cap.next()
        #print ('%s: captured %d bytes, truncated to %d bytes' %(datetime.datetime.now(), header.getlen(), header.getcaplen()))
        parse_packet(packet)

#Convert a string of 6 characters of ethernet address into a dash separated hex string
def eth_addr (a) :
    '''
    open device
    # Arguments here are:
    #   resolve eth addr into readable format
    '''
    b = "%.2x:%.2x:%.2x:%.2x:%.2x:%.2x" % (ord(a[0]) , ord(a[1]) , ord(a[2]), ord(a[3]), ord(a[4]) , ord(a[5]))
    return b

def search_dictionary(search_value):
    '''
    open device
    # Arguments here are:
    # Dictionary lookup
    '''
	for key, value in global_dict.items():
		if value == search_value:
			return True
        else: return False

#function to parse a packet
def parse_packet(packet) :
    '''
    open device
    # Arguments here are:
    #   Packet to define
    '''
    #parse ethernet header
    eth_length = 14

    eth_header = packet[:eth_length]
    eth = unpack('!6s6sH' , eth_header)
    eth_protocol = socket.ntohs(eth[2])
    print 'Destination MAC : ' + eth_addr(packet[0:6]) + ' Source MAC : ' + eth_addr(packet[6:12]) + ' Protocol : ' + str(eth_protocol)

    #Parse IP packets, IP Protocol number = 8
    if eth_protocol == 8 :
        #Parse IP header
        #take first 20 characters for the ip header
        ip_header = packet[eth_length:20+eth_length]

        #now unpack them :)
        iph = unpack('!BBHHHBBH4s4s' , ip_header)

        version_ihl = iph[0]
        version = version_ihl >> 4
        ihl = version_ihl & 0xF

        iph_length = ihl * 4

        ttl = iph[5]
        protocol = iph[6]
        s_addr = socket.inet_ntoa(iph[8])
        s_addr = s_addr + ' ' + eth_addr(packet[6:12])
        d_addr = socket.inet_ntoa(iph[9])
        d_addr = d_addr + " " + eth_addr(packet[0:6])

        print str(protocol) + ' Source Address : ' + str(s_addr) + ' Destination Address : ' + str(d_addr)
        #*******EVENTS***********
        # Too add: add location resolver to flag russia, eeu, and china IP prefixes 
        if socket.inet_ntoa(iph[8]).startswith("192.168.2") and not socket.inet_ntoa(iph[9]).startswith("192.168.1.163"): # if DMZ is communicating with anything other than load balancer
            print ("DMZ BROKEN") #neeed to add email alert
            flagged_dict['Event'] = 'DMZ broken'
            flagged_dict['Source Addresses'] = s_addr
            flagged_dict['Destination Addresses'] = d_addr
        if search_dictionary(socket.inet_ntoa(iph[8])) == False:
            global_dict['source addresses']= s_addr # update dict
            geoip_search(socket.inet_ntoa(iph[8])) # resolve country of origin
            # need to add sqlite3 db update from dictionary here
            conn = sqlite3.connect('backend.db')
            cursor.execute("""UPDATE flaggedDIP SET DIP = ? ,SIP = ?,DMAC = ?,SMAC = ? """,(socket.inet_ntoa(iph[8]),socket.inet_ntoa(iph[9]),eth_addr(packet[6:12]),eth_addr(packet[0:6])))
            #cur.execute("INSERT INTO Current_Traffic VALUES(socket.inet_ntoa(iph[8]),socket.inet_ntoa(iph[9]), eth_addr(packet[6:12]), eth_addr(packet[0:6]))")
        elif search_dictionary(socket.inet_ntoa(iph[9])) == False:
            conn = sqlite3.connect('backend.db')
            global_dict['destination addresses']= d_addr # update dict
            geoip_search(socket.inet_ntoa(iph[9])) # resolve country of origin
            # need to add sqlite3 db update from dictionary here
            cursor.execute("""UPDATE flaggedSIP SET DIP = ? ,SIP = ?,DMAC = ?,SMAC = ? """,(socket.inet_ntoa(iph[8]),socket.inet_ntoa(iph[9]),eth_addr(packet[6:12]),eth_addr(packet[0:6])))
            #cur.execute("INSERT INTO Current_Traffic VALUES(socket.inet_ntoa(iph[8]),socket.inet_ntoa(iph[9]), eth_addr(packet[6:12]), eth_addr(packet[0:6]))")
        else: print ('IPs already known' + s_addr + d_addr)

if __name__ == "__main__":
  main(sys.argv)
