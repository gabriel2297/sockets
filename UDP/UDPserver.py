# import the sockets library
from socket import *

# port where the server is listening for requests
serverPort = 12000

# here we bind the IP address to the transport layer protocol. 
# :param AF_INET: tells the underlying OS to get the IP address of the host
# :param SOCK_DGRAM: tells the OS this is a UDP datagram
serverSocket = socket(AF_INET, SOCK_DGRAM) 

# bind the serverPort to the socket, this way the server will always be working in port 12000
serverSocket.bind(('', serverPort))

# print a message
print "The server is ready to receive"

# execute forever
while 1:
    # save the data we receive into a message variable. Also save the client's IP and port (clientAddress). Used to return traffic
    message, clientAddress = serverSocket.recvfrom(2048) 
    # print that we received something and the received message
    print "Message received: %s" % message
    # make each letter in the message caps. 
    modifiedMessage = message.upper() 
    # print the response
    print "We'll respond: %s" % modifiedMessage 
    # send the message back to the client 
    serverSocket.sendto(modifiedMessage, clientAddress)