# import the socket library 
from socket import *

# the server name, in this case we'll use localhost to use
# our own IP address
serverName = 'localhost'

# the port where the server will be listening for requests
serverPort = 12000

# create a TCP socket with an IPv4 address and use the 
# the socket is of type TCP (not UDP)
clientSocket = socket(AF_INET, SOCK_STREAM) 

# make a TCP connection to the client at the specified port
# initiates the 3-way handshake process
clientSocket.connect((serverName,serverPort)) 

# get data from console
sentence = raw_input('Input lowercase sentence: ') 

# instead of creating a packet like in UDP and just sending it, 
# the socket will send the sentence into the TCP connection and 
# wait for a response
clientSocket.send(sentence)

# get what the server responds and save it in another variable
modifiedSentence = clientSocket.recv(1024) 

# print what we got
print 'From Server: ', modifiedSentence

# close the TCP connection
clientSocket.close()